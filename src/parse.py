
import numpy as np
import sys

class Parse:
    def __init__(self, PDBs):
        self.PDB = PDBs
        
    def coordinates(self, output):
        x = []
        y = []
        z = []
        
        try:
            with open(self.PDB) as file:            
                for line in file:
                    if line.startswith("ATOM"):
                        coord_x = line[30:38]
                        x.append(float(coord_x))

                        coord_y = line[38:46]
                        y.append(float(coord_y))

                        coord_z = line[46:54]
                        z.append(float(coord_z))
                
            arr_x = np.array(x)
            arr_y = np.array(y)
            arr_z = np.array(z)
                
            arr = np.stack((arr_x, arr_y, arr_z), axis=1)
        
        except:
            print("Failed to parse file. File empty or excesive atom information")
            sys.exit(1)
                
        np.savetxt(output, arr)
