#!/bin/python3
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --partition=RT_build
#SBATCH --job-name=Kalinichev_test
#SBATCH --comment="commnet for Kalinichev"
###SBATCH -s

import multiprocessing as mp
import sys
import os
# Necessary to add cwd to path when script run
# by SLURM (since it executes a copy)
sys.path.append(os.getcwd())
#### import plotly.express as px
def read_dump(filename):
        f=open(filename,"r")
        lines = f.readlines()
        coord_of_time=dict()
        while len(lines)>0:
                step=int(lines[1])
                N=int(lines[3])
                line_wall = lines[5].split()
                wall = float(line_wall[1])
                coordinates=dict()
                for i in range(N):
                        line_from_split = lines[9+i].split()
                        id_of_atom=int(line_from_split[0])
                        type_of_atom=int(line_from_split[1])
                        x=float(line_from_split[2])
                        y=float(line_from_split[3])
                        z=float(line_from_split[4])
                        r=[x,y,z]
                        coordinates[id_of_atom] = [type_of_atom, r]
                coord_of_time[step]=coordinates
                lines=lines[(9+N):]
        return coord_of_time
def check_border_intersec(i,j,step,border_intersec,data):
    x=dict()
    for k in range(3):
        x[k]=data[i][j][1][k]-data[max(i-step,0)][j][1][k]
        if(x[k]>0.5):
            border_intersec[j][k]+=1
        if(x[k]<-0.5):
            border_intersec[j][k]-=1
def MSD_calculator(args):
    data=read_dump(args[0])
    step=100
    N=len(data[0])
    MSD=dict()
    x=[0,0,0]
    border_intersec=dict()
    for j in range(1,len(data[0])+1):
        border_intersec[j]=[0,0,0]
    for i in range(0,3000,step):
        MSD[i]=0
        for j in range(1,len(data[i])+1):
            check_border_intersec(i,j,step,border_intersec,data)
            for k in range(3):
                x[k]=data[i][j][1][k]-data[0][j][1][k]-border_intersec[j][k]
            MSD[i]+=x[0]*x[0]+x[1]*x[1]+x[2]*x[2]
        MSD[i]=MSD[i]/N
    return [args[1],MSD]
file_list = [ ["lj/diam_{:s}/dump.shear.void".format(i),i] for i in ["2.0","2.5","3.0","3.5","4.0"] ]
with mp.Pool(4) as p:
    data=p.map(MSD_calculator, file_list)
data = sorted(data, key=lambda x: x[0])
import pickle
with open("dump.pickle", "wb") as f:
    pickle.dump(data, f)