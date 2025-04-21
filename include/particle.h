// particle.h

#ifndef PARTICLE_H
#define PARTICLE_H

typedef struct { // creates the structure for each "particle" in the system, used name particle because body got confusing
    double mass;
    double x, y, z;  // Position
    double vx, vy, vz;  // Velocity
    double ax, ay, az; // Acceleration
    double ax0, ay0, az0; // Pre Drift Acceleration
} Particle;

#endif // PARTICLE_H