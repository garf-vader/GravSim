The Python files are various Data Analysis, Visualisation, and QoL features. 
They require an environment that may be initialised using requirements.txt.

Plotter.py is commented out, as I didnt directly save the output plots to files, I saved from the UI

speedtest.sh might work but I never got access to an HPC for this specific project


How to build the C code:

	There are 3 makefiles
	use "make -f solar.mk" and "make -f speed.mk" to create the solar and speedtest executable
	do not run makefile.mk, it is for HPC but I never ran this specific code on one
	
	You will need the gcc compiler on your system

It isnt the most intuitive how I got the data I got for the solar system because I just fiddled around a bit with variables, some gravity datasets are also available.


The data is saved periodically to a file, there is a multiplier used to control this, otherwise the exported txt file will be of the order of a 100+ MB