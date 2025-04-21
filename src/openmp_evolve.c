// openmp_evolve.c

#include "particle.h"
#include "openmp_evolve.h"

#include <stdio.h>
#include <math.h>
#include <omp.h>

//
// OpenMP Code
//

void calculate_accel_openmp(Particle particles[], int num_particles, double G) {
    int i, j;
    double dx, dy, dz, distance, force_magnitude;

    #pragma omp parallel for private(i, j, dx, dy, dz, distance, force_magnitude) shared(particles, num_particles) schedule(dynamic)
    for (i = 0; i < num_particles; ++i) {
        double ax_private = 0.0, ay_private = 0.0, az_private = 0.0;
        particles[i].ax0 = particles[i].ax;
        particles[i].ay0 = particles[i].ay;
        particles[i].az0 = particles[i].az;

        #pragma omp simd reduction(+:ax_private,ay_private,az_private)
        for (j = 0; j < num_particles; ++j) {
            if (i != j) {
                dx = particles[j].x - particles[i].x;
                dy = particles[j].y - particles[i].y;
                dz = particles[j].z - particles[i].z;

                distance = sqrt((dx * dx) + (dy * dy) + (dz * dz));
                // particle i mass cancels when you calculate accel anyway so it can be left out of equation to save compute time
                force_magnitude = G * particles[j].mass / (distance * distance);

                // Calculate acceleration components
                ax_private += force_magnitude * (dx / distance);
                ay_private += force_magnitude * (dy / distance);
                az_private += force_magnitude * (dz / distance);

                //#pragma omp atomic // left these lines to show the bad way to handle shared memory, with 0 caching
                //particles[i].ax += force_magnitude * (dx / distance);
                //#pragma omp atomic
                //particles[i].ay += force_magnitude * (dy / distance);
                //#pragma omp atomic
                //particles[i].az += force_magnitude * (dz / distance);
            }
        }
        // Update values outside j loop, quicker than atomic
        particles[i].ax = ax_private;
        particles[i].ay = ay_private;
        particles[i].az = az_private;
    }
}

void evolve_openmp(Particle particles[], int num_particles, double dt, double G) {
    int i;
    double half_dt = 0.5 * dt; // define this variable to avoid repeat calculations

    calculate_accel_openmp(particles, num_particles, G); // calculate acceleration

    #pragma omp parallel for private(i) shared(particles, num_particles, dt)
    for (i = 0; i < num_particles; ++i) {
        particles[i].vx += particles[i].ax0 * half_dt; // kick x
        particles[i].vy += particles[i].ay0 * half_dt; // kick y
        particles[i].vz += particles[i].az0 * half_dt; // kick z

        particles[i].x += particles[i].vx * dt; // drift x
        particles[i].y += particles[i].vy * dt; // drift y
        particles[i].z += particles[i].vz * dt; // drift z

        particles[i].vx += particles[i].ax * half_dt; // kick x
        particles[i].vy += particles[i].ay * half_dt; // kick y
        particles[i].vz += particles[i].az * half_dt; // kick z
    }
}