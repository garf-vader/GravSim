#include "particle.h"

#include "openmp_evolve.h"
#include "initialiser.h"

#include <time.h>

int main() {
    double dt = 3600;
    double G = 6.67430 * pow(10, -11);
    int steps = 87600; // with this dt 8760 is 1 years

    int num_particles = 83;  // Number of particles
    Particle particles[num_particles]; // Create empty structure
    char filename[] = "solar_system_data/initial_conditions.txt";

    omp_set_num_threads(6);

    // Read particle information from input
    initialise(num_particles, particles, filename);

    clock_t begin = clock();

    calculate_accel_openmp(particles, num_particles, G);

    for (int i = 0; i < num_particles; ++i) {
        if(isnan(particles[i].ax+particles[i].ay+particles[i].az)) {
            printf("Particle %d: x=%f, y=%f, z=%f\n", i+1, particles[i].ax, particles[i].ay, particles[i].az);
        }
    } // useful for determining if errors have been caused by incorrect initial values (returns objects with nan initial accel)
    

    // Calculate forces between particles
    FILE* results = fopen("solar_system_data/serial_pos.txt", "w");
    for (int i = 0; i < steps; ++i) {
        if (i%24 == 0) { // exports the position of every body every 24 steps, useful for reducing filesize
            for (int j = 0; j < num_particles; ++j) {
                fprintf(results, "%f %f %f %f ", particles[j].mass, particles[j].x, particles[j].y, particles[j].z);
            }
            fprintf(results, "\n");
        }
        evolve_openmp(particles, num_particles, dt, G);
    }
    fclose(results);

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

    printf("Particle 1: x=%f, y=%f, z=%f\n", particles[5].x, particles[5].y, particles[5].z);
    printf("Time Taken: %f\n", time_spent);

    return 0;
}