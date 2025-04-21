python virtual environment is there for the python files
If you dont want to use the venv then you can just make sure you have the python modules needed globally and run the code

plotter.py is commented out, as I didnt directly save the output plots to files, I saved from the UI
speedtest.sh might work but I never got access to bluecrystal


How to build the C code:

	There are 3 makefiles
	use "make -f solar.mk" and "make -f speed.mk" to create the solar and speedtest executable
	do not run makefile.mk, it was for BlueCrystal but I never got access
	
	You will need the gcc compiler on your system

It isnt the most intuitive how I got the data I got because I just fiddled around a bit with variables

If you change steps in make sure you adjust the multiplier for index of the if statement that saves data to file

If that multiplier isnt large enough the exported txt file will be of the order of a 100+ MB

I deleted serial_pos.txt as its 50MB but if plotter fails thats why, run solar.exe first