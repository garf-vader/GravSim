# Gravity Simulator (GravSim)
## Project Notes

This project includes a mix of data analysis, visualization tools, and performance-oriented simulations in both Python and C.

### 🐍 Python Scripts

The Python files offer various utilities for:

- Data Analysis
- Visualization
- Quality-of-Life Enhancements

These scripts require a virtual environment initialized with the `requirements.txt` file.

Note:
The `plotter.py` script is currently commented out. While it was used to generate visualizations, the plots were saved manually from the UI rather than being written to files programmatically.

### 🚀 C Simulation Code

The C code is focused on numerical simulations (e.g., planetary motion) and includes specific performance enhancements.

#### Building the Code

Three Makefiles are included:

- `make -f solar.mk`: Compiles the solar simulation executable.
- `make -f speed.mk`: Compiles the speedtest benchmarking tool.
- `make -f makefile.mk`: Intended for HPC use but has not been tested in this context.

⚠️ You will need the GCC compiler installed on your system to build the executables.

#### Speed Considerations

- The `speedtest.sh` script was meant for testing on HPC systems but was never fully deployed due to lack of access.
- Periodic data exports can result in large files (100+ MB). A multiplier is used to control the save frequency and mitigate this.

#### Performance Optimizations

- Distance Calculations Optimized:
  By pre-calculating `1/distance` and `distance²`, the algorithm avoids repeated divisions.
  This results in a:
    - Reduction from 3 divisions + 1 multiplication
    - To 3 multiplications + 1 division
  Achieving up to 25% speedup in simulation performance.

### 🔬 Data Sources & Setup

Some gravity datasets were used during experimentation, but the exact methodology was exploratory and iterative—variables were adjusted through trial and error to produce meaningful solar system simulations.
