import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def time_compare():
    fig, ax1 = plt.subplots(figsize=(10, 10))
    ax1.set_xlim(56, 1032)

    plt.title("Time to evolve simulation 5000 times")
    serial_filename = "time_data/serial_bigO.txt"
    openmp_filename = "time_data/openmp_bigO.txt"
    serial = np.loadtxt(serial_filename)
    openmp = np.loadtxt(openmp_filename)
    ax1.plot(serial[:, 0], serial[:, 1], "-k", label = "Serial")
    ax1.plot(openmp[:, 0], openmp[:, 1], "-b", label = "OpenMP")

    ax1.set_ylim(0, 32)
    ax1.set_xlabel("N")
    ax1.set_ylabel("t (s)")
    ax1.legend(loc='upper left')

    #plt.title("Relative time taken to compute 1000 evolutions by number of bodies")
    ax2 = ax1.twinx()
    ax2.set_ylim(0, 6)
    ax2.plot(serial[:, 0], serial[:, 1]/openmp[:, 1], "--bo")

    ax2.set_ylabel("S")


##############################################################


def animate(i, scat, data):
    m, x, y, z = data[i].T
    scat.set_offsets(np.c_[x, y])
    return scat


def animate_model():
    filename = "solar_system_data/serial_pos.txt"
    data = np.loadtxt(filename)
    data = np.reshape(data, (-1, 83, 4))

    fig, ax = plt.subplots(figsize=(12, 12))
    """ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])"""

    ax.set_xlim([-1*10**12, 1*10**12])
    ax.set_ylim([-1*10**12, 1*10**12])

    m, x, y, z = data[0].T
    #scale_factor = ((np.log10(m)/np.min(np.log10(m))))**6 #nothing scientific here, just looks nicer scaled with mass
    scale_factor = m**(1/5) / np.min(m**(1/5))/10
    scat = plt.scatter(x, y, c="black", s=scale_factor)

    ani = FuncAnimation(
        fig,
        animate,
        fargs=(scat, data),
        repeat=False,
        frames=data.shape[0],
        interval=0,
        cache_frame_data=False,
    )

    ani.save("solar.mp4", fps=75)


##############################################################

def earth_orbit():
    filename = "solar_system_data/serial_pos.txt"
    data = np.loadtxt(filename)
    data = np.reshape(data, (-1, 83, 4))

    earth_data = data[:,5,:]

    x, y, z = earth_data[:,1], earth_data[:,2], earth_data[:,3]

    dist = np.sqrt(x**2+y**2+z**2)

    plt.plot(dist)

#############################################################

def plot_3d():
    filename = "solar_system_data/serial_pos.txt"
    data = np.loadtxt(filename)
    data = np.reshape(data, (-1, 83, 4))

    plt.rcParams['grid.color'] = (0.5, 0.5, 0.5, 0.2)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')

    ax.set_xlim([-1*10**12, 1*10**12])
    ax.set_ylim([-1*10**12, 1*10**12])

    # remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # set color to white

    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    m, x, y, z = data[365].T # choose the state of the system in 1 year
    scale_factor = m**(1/5) / np.min(m**(1/5))/10
    ax.scatter(x, y, z, c="black", s=scale_factor)

def plot_2d():
    filename = "solar_system_data/serial_pos.txt"
    data = np.loadtxt(filename)
    data = np.reshape(data, (-1, 83, 4))

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot()
    """ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])"""

    ax.set_xlim([-1*10**12, 1*10**12])
    ax.set_ylim([-1*10**12, 1*10**12])


    # Bonus: To get rid of the grid as well:
    #ax.grid(False)

    m, x, y, z = data[365].T # choose the state of the system in 1 year
    scale_factor = m**(1/5) / np.min(m**(1/5))/10
    ax.scatter(x, y, c="black", s=scale_factor) 

def thread_graph():
    fig, ax1 = plt.subplots(figsize=(10, 10))
    #ax1.set_xlim(56, 1032)

    plt.title("Relative time spent computing")
    thread = "time_data/thread_time.txt"
    thread_time = np.loadtxt(thread)
    ax1.plot(thread_time[:, 0], thread_time[:, 1]*thread_time[:, 0]/thread_time[0, 1], "-bo")


    #ax1.set_ylim(0, 2)
    ax1.set_xlabel("threads")
    ax1.set_ylabel("t (s)")

#time_compare()
#animate_model() # commented out as I saved the graphs manually instead of by function
#earth_orbit()
#plot_3d()
#plot_2d()
#thread_graph()