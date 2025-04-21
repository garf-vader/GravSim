#include "particle.h"
#include "initialiser.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//
// Import code
//

void parse_line(char* line, Particle* particle) {
    sscanf(line, "%lf %lf %lf %lf %lf %lf %lf",
           &particle->mass,
           &particle->x, &particle->y, &particle->z,
           &particle->vx, &particle->vy, &particle->vz);
           // mass, x, y, z, vx, vy, vz for particle i, accel is empty
}

//
// The following function initialises an N body system, this must be called multiple times therefore I made it a function
//

void initialise(int num_particles, Particle particles[], char filename[]) {
    FILE* file = fopen(filename, "r");
    // Read particle information from input
    // Lazilly just running this for both serial and parallel, could clone the structure after...
    // reading but it is really not very time intensive to just recreate the sturcture every time
    char buffer[256];  // Adjust the buffer size as needed
    for (int i = 0; i < num_particles; ++i) {
        if (fgets(buffer, sizeof(buffer), file) == NULL) {
            fprintf(stderr, "Error reading input.\n");
            fclose(file);
        }
        parse_line(buffer, &particles[i]);
    }                                    
    fclose(file);
}