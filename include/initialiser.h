#ifndef INITIALISER_H
#define INITIALISER_H

#include "particle.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void parse_line(char* line, Particle* particle);

void initialise(int num_particles, Particle particles[], char filename[]);

#endif  // INITIALISER_H