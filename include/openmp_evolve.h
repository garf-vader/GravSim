// openmp_evolve.h

#ifndef OPENMP_EVOLVE_H
#define OPENMP_EVOLVE_H

#include "particle.h"
#include <stdio.h>
#include <math.h>
#include <omp.h>


void calculate_accel_openmp(Particle particles[], int num_particles, double G);
void evolve_openmp(Particle particles[], int num_particles, double dt, double G);

#endif