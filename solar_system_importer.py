# this programme shows 0 technical skill but it is here incase the solar_system_data folder is lost
# running this will create 2 files
# initial_conditions.txt - An 83x7 array whitespace delimited txt file of initial mass, x, y, z, vx, vy, vz
#                           of solar system objects, x, y, z, vx, vy, vz retrieved from JPL Horizons API
# names.txt              - An 83 line txt file which can be used to find the index of the solar system objects by name

import numpy as np
from horizons_importer import importer

solar_objects_83 = [
    ["Sun", 1.989e30, "10"],
    ["Jupiter", 1.898e27, "599"],
    ["Saturn", 5.683e26, "699"],
    ["Neptune", 1.024e26, "899"],
    ["Uranus", 8.681e25, "799"],
    ["Earth", 5.972e24, "399"],
    ["Venus", 4.867e24, "299"],
    ["Mars", 6.417e23, "499"],
    ["Mercury", 3.301e23, "199"],
    ["Ganymede", 1.4819e23, "503"],
    ["Titan", 1.3455e23, "606"],
    ["Callisto", 1.0759e23, "504"],
    ["Io", 8.932e22, "501"],
    ["Moon", 7.342e22, "301"],
    ["Europa", 4.8e22, "502"],
    ["Triton", 2.14e22, "801"],
    ["Pluto", 1.303e22, "134340"],
    ["Eris", 1.66e22, "136199"],
    ["Haumea", 4.006e21, "136108"],
    ["Titania", 3.4e21, "703"],
    ["Makemake", 3.1e21, "136472"],
    ["Oberon", 3.08e21],
    ["Rhea", 2.307e21],
    ["Iapetus", 1.806e21],
    ["Gonggong", 1.75e21],
    ["Charon", 1.586e21],
    ["Umbriel", 1.28e21],
    ["Ariel", 1.25e21],
    ["Quaoar", 1.2e21, "50000"],
    ["Dione", 1.095e21],
    ["Ceres", 9.393e20],
    ["Tethys", 6.17e20],
    ["Salacia", 4.92e20, "120347"],
    ["Sedna", 1.5e21, "90377"],
    ["Orcus", 6.32e20, "90482"],
    ["Vesta", 2.59076e20],
    ["Pallas", 2.11081e20],
    ["Hygiea", 8.67e19],
    ["Interamnia", 2.727e19, "A910 TC"],
    ["Psyche", 2.72e19, "A852 FA"],
    ["Davida", 2.9e19, "511"],
    ["Ida", 4.2e16, "243"],
    ["Eros", 6.69e15, "433"],
    ["Amphitrite", 1.27e19, "29"],
    ["Herculina", 1.29e19, "532"],
    ["Massalia", 5.2e18],
    ["Kalliope", 8e18],
    ["Camilla", 1.12e19],
    ["Euphrosyne", 1.03e19],
    ["Bamberga", 1.59e18],
    ["Cybele", 1.5E+19, "A861 EB"],
    ["Irene", 1.45E+17],
    ["Egeria", 3.18e18],
    ["Eugenia", 1.19e17],
    ["Antiope", 1.19e17],
    ["Thalia", 1.96e18],
    ["Juno", 2.86e19, "A804 RA"],
    ["Eunomia", 3.05e19],
    ["Thisbe", 1.5e19],
    ["Iris", 1.375e19, "A847 PA"],
    ["Lutetia", 1.7e18],
    ["Parthenope", 5.5e18],
    ["Lachesis", 5.5e18],
    ["Mnemosyne", 1.26e19],
    ["Aurora", 6.2e18],
    ["Leukothea", 7.92e17],
    ["Atalante", 4.32e18],
    ["Fides", 1.3e18],
    ["Harmonia", 1.3e18],
    ["Hestia", 3.5e18],
    ["Maja", 1.8e17],
    ["Asia", 1.03e18],
    ["Pomona", 7.5e17],
    ["Frigga", 1.74e18],
    ["Nysa", 3.7e17],
    ["Feronia", 3.32e18, "A861 KA"],
    ["Eos", 5.87e18, "A882 BA"],
    ["Diana", 1.27e18],
    ["Astraea", 2.9e18],
    ["Metis", 1e19],
    ["Amalthea", 2.08e18],
    ["Thebe", 7.77e17],
    ["Dysnomia", 8.2e19],
]

body_names = []
bodies = []

for object in solar_objects_83:
    if len(object) == 3:
        name, pos, vel = importer(object[2])
    else:
        name, pos, vel = importer(object[0])
    body_names.append(object[0])
    bodies.append([object[1], pos[0], pos[1], pos[2], vel[0], vel[1], vel[2]])

np.savetxt("solar_system_data/names.txt", np.array(body_names), fmt='%s')
np.savetxt("solar_system_data/initial_conditions.txt", np.array(bodies))

# pos and vel entered in km and km/s but converted before saving
# this is because data is from Horizons system

# for the sake of testing I will model the major bodies of the solar system and
# determine the accuracy and speed of the simulation