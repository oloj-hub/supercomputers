import numpy as np

def read_lammpstrj(filename):
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
                        r=np.array([x,y,z])
                        coordinates[id_of_atom] = [type_of_atom, r]
                coord_of_time[step]=[wall, coordinates]
                lines=lines[9+N:]
                print (step)
        return coord_of_time

data = read_lammpstrj("eff_h2.nve.lammpstrj")

print ("len of data: ", len(data))
