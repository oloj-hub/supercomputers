#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=8
#SBATCH --partition=RT
#SBATCH --job-name=lammps_fedoorv
#SBATCH --comment="Fedorov Lammps test"
srun ~/bin/lmp_mpi -in in.h2bulk.nve
