# I abandoned python for the actual calculations after creating this, 
# but I leave it here as a handy comparison of the efficiency of Python vs C
# This was about as fast as I could make the Python simulator without delving into BLAS

import numpy as np
from numpy.linalg import norm 
import time

def system_gen(filename): # creates standardised, sorted, list of attributes for each body
    # any csv file formatted mass, x, y, z, vx, vy, vz will work distance in km, velocity in km/s, mass in kg*10^24
    data = np.loadtxt(filename)

    masses = data[:, 0]
    positions = data[:,1:4]
    velocities = data[:,4:7]

    mass_matrix = masses.reshape((1, -1, 1)) * masses.reshape((-1, 1, 1))

    return masses, mass_matrix, positions, velocities

def acc_vect(positions, masses, mass_matrix, G):
    disps = positions.reshape((1, -1, 3)) - positions.reshape((-1, 1, 3))  # displacements
    dists = norm(disps, axis=2)
    dists[dists == 0] = 1  # Avoid divide by zero warnings
    forces = G * disps * mass_matrix / (np.expand_dims(dists, 2)) ** 3
    return forces.sum(axis=1) / masses.reshape(-1, 1)


def evolve(x, v, m, mm, a, G, dt):
    v = v + 0.5 * a * dt # kick
    x = x + v * dt # drift
    a = acc_vect(x, m, mm, G) # calculate acceleration
    v = v + 0.5 * a * dt # kick

    return x, v, a


def total_energy(masses, pos, vels, G): # this function is horribly slow, perhaps only run on every tenth step
    ke = []
    gpe = []
    for v in vels:
        ke.append(0.5 * masses * norm(v, axis=1) ** 2)
    for p in pos:
        mass_matrix = masses.reshape((1, -1, 1)) * masses.reshape((-1, 1, 1))

        for i in range(len(mass_matrix[0])):
            mass_matrix[i][i] = 0

        disps = p.reshape((1, -1, 3)) - p.reshape((-1, 1, 3))  # displacements
        dists = norm(disps, axis=2)
        dists[dists == 0] = 1  # Avoid divide by zero warnings
        potential = -G * mass_matrix / np.expand_dims(dists, 2)
        gpe.append(np.squeeze(potential.sum(axis=1)))

    ke = np.array(ke).sum(axis=1)
    gpe = np.array(gpe).sum(axis=1) / 2

    total_e = ke + gpe
    return total_e, ke, gpe

def restart(G):
    masses, mass_matrix, positions, velocities = system_gen("c_codefiles/tab1024.txt")
    pos_history = []
    vel_history = []
    accelerations = acc_vect(positions, masses, mass_matrix, G)
    return masses, mass_matrix, positions, velocities, pos_history, vel_history, accelerations


steps = 1000
dt = 0.00002
G = 1 #6.67430 * 10 ** (-11)
masses, mass_matrix, positions, velocities, pos_history, vel_history, accelerations = restart(G)

start = time.perf_counter()
for n in range(steps):
    positions, velocities, accelerations = evolve(
        positions, velocities, masses, mass_matrix, accelerations, G, dt
    )
    #pos_history.append(positions)
    #vel_history.append(velocities)

end = time.perf_counter() - start
print(f"Speed: {end}")

#total_e_system, ke, gpe = total_energy(masses, pos_history, vel_history, G)


#print(f"Time:{(time.perf_counter()-start)/steps}")

#directory = "128_system_test"

#np.save(f"{directory}/pos_history", pos_history)
#np.save(f"{directory}/vel_history", vel_history)
#np.save(f"{directory}/total_e_system", total_e_system)
#np.save(f"{directory}/ke", ke)
#np.save(f"{directory}/gpe", gpe)