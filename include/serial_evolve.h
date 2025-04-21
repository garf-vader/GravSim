// serial_evolve.h

#ifndef SERIAL_EVOLVE_H
#define SERIAL_EVOLVE_H

#include "particle.h"
#include <stdio.h>
#include <math.h>

void calculate_accel_serial(Particle particles[], int num_particles, double G);
void evolve_serial(Particle particles[], int num_particles, double dt, double G);

#endif