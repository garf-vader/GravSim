#include "particle.h"

#include "serial_evolve.h"
#include "openmp_evolve.h"
#include "initialiser.h"

#include <time.h>

// this version of the code runs for a range of N values and 
// outputs only the time taken to evolve the simulation for 1000 steps

// this version contains a non parallel code
// it outputs a txt file, a list of N values and the time taken to evolve 1000 steps

// this data can then be plotted using matplotlib in the plotter.py programme
// plotter.py is configured by me to just run every plot I want and save them to files
// but if needed plotter.py could easily be made interactive or turned into a callable function

int main() {
    // my CPU is a Ryzen 5 3600
    // My CPU base speed is 3.6 GHz, BlueCrystal is 2.4 GHz
    // If I don't get around to uploading the job to BlueCrystal I can generate data using my CPU

    omp_set_num_threads(6);

    double dt = 0.00002;
    int steps = 1000;
    double G = 1;

    char filename[] = "tab1024.txt";
    int N_vals[16] = {64, 128, 192, 256, 320, 384, 448, 512, 576, 640, 704, 768, 832, 896, 960, 1024};

    FILE* serial_results = fopen("time_data/serial_bigO.txt", "w");
    for (int i = 0; i < 16; ++i) {
        int num_particles = N_vals[i];
        Particle particles[num_particles]; // Create empty structure
        initialise(num_particles, particles, filename);

        clock_t begin = clock();

        calculate_accel_serial(particles, num_particles, G); // Calculate initial accelerations

        // Calculate forces between particles
        for (int i = 0; i < steps; ++i) {
            evolve_serial(particles, num_particles, dt, G);
        }

        clock_t end = clock();
        double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

        // Prints the time spent to both the output and a results file so it can be plotted using matplotlib
        printf("Time Taken: %f\n", time_spent);
        fprintf(serial_results,"%d %f\n", num_particles, time_spent);
    }
    fclose(serial_results);

    FILE* openmp_results = fopen("time_data/openmp_bigO.txt", "w");
    for (int i = 0; i < 16; ++i) {
        int num_particles = N_vals[i];
        Particle particles[num_particles]; // Create empty structure
        
        initialise(num_particles, particles, filename);

        clock_t begin = clock();

        calculate_accel_openmp(particles, num_particles, G); // Calculate initial accelerations

        // Calculate forces between particles
        for (int i = 0; i < steps; ++i) {
            evolve_openmp(particles, num_particles, dt, G);
        }

        clock_t end = clock();
        double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

        // Prints the time spent to both the output and a results file so it can be plotted using matplotlib
        printf("Time Taken: %f\n", time_spent);
        fprintf(openmp_results,"%d %f\n", num_particles, time_spent);
    }
    fclose(openmp_results);

    FILE* thread_results = fopen("time_data/thread_time.txt", "w");
    for (int i = 1; i < 6; ++i) {
        omp_set_num_threads(i);
        int num_particles = 1024;
        Particle particles[num_particles]; // Create empty structure
        
        initialise(num_particles, particles, filename);

        clock_t begin = clock();

        calculate_accel_openmp(particles, num_particles, G); // Calculate initial accelerations

        // Calculate forces between particles
        for (int i = 0; i < steps; ++i) {
            evolve_openmp(particles, num_particles, dt, G);
        }

        clock_t end = clock();
        double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

        // Prints the time spent to both the output and a results file so it can be plotted using matplotlib
        printf("Time Taken: %f\n", time_spent);
        fprintf(thread_results,"%d %f\n", i, time_spent);
    }
    fclose(thread_results);

    return 0;
}