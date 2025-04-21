#!/bin/bash
# =================
# speedtest.sh
# =================
#SBATCH --job-name=test_job
#SBATCH --partition=teach_cpu
#SBATCH --account=PHYS030385
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=28
#SBATCH --time=0:5:00
#SBATCH --mem=600M
# Load modules required for runtime e.g.
module load languages /intel/2020-u4

cd $SLURM_SUBMIT_DIR
export OMP_NUM_THREADS=$ {SLURM_CPUS_PER_TASK}

# Now run you r program w it h the u sual command
./bin/speedtest