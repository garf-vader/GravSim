// serial_evolve.c

#include "particle.h"
#include "serial_evolve.h"

#include <stdio.h>
#include <math.h>

// this version of the code runs for a range of N values and 
// outputs only the time taken to evolve the simulation for 1000 steps

// this version contains a non parallel code
// it outputs a txt file, a list of N values and the time taken to evolve 1000 steps

// this data can then be plotted using matplotlib in the plotter.py programme
// plotter.py is configured by me to just run every plot I want and save them to files
// but if needed plotter.py could easily be made interactive or turned into a callable function

//
// Serial Code
//

void calculate_accel_serial(Particle particles[], int num_particles, double G) {
    int i, j;
    double dx, dy, dz, distance, force_magnitude;

    for (i = 0; i < num_particles; ++i) {
        particles[i].ax = 0;
        particles[i].ay = 0;
        particles[i].az = 0;
        for (j = 0; j < num_particles; ++j) {
            if (i != j) {
                dx = particles[j].x - particles[i].x;
                dy = particles[j].y - particles[i].y;
                dz = particles[j].z - particles[i].z;

                distance = sqrt((dx * dx) + (dy * dy) + (dz * dz));
                // particle i mass cancels when you calculate accel anyway so it can be left out of equation to save compute time
                force_magnitude = G * particles[j].mass / (distance * distance);

                // Calculate acceleration components
                particles[i].ax += force_magnitude * (dx / distance);
                particles[i].ay += force_magnitude * (dy / distance);
                particles[i].az += force_magnitude * (dz / distance);
            }
        }
    }
}

void evolve_serial(Particle particles[], int num_particles, double dt, double G) {
    int i;
    double half_dt = 0.5 * dt; // define this variable to avoid repeat calculations

    for (i = 0; i < num_particles; ++i) {
        particles[i].vx += particles[i].ax * half_dt; // kick x
        particles[i].vy += particles[i].ay * half_dt; // kick y
        particles[i].vz += particles[i].az * half_dt; // kick z

        particles[i].x += particles[i].vx * dt; // drift x
        particles[i].y += particles[i].vy * dt; // drift y
        particles[i].z += particles[i].vz * dt; // drift z
    }

    calculate_accel_serial(particles, num_particles, G); // calculate acceleration
    // this version is serial therefore exiting and entering loops is quicker than assigning 3 new variables

    for (i = 0; i < num_particles; ++i) {
        particles[i].vx += particles[i].ax * half_dt; // kick x
        particles[i].vy += particles[i].ay * half_dt; // kick y
        particles[i].vz += particles[i].az * half_dt; // kick z
    }
}