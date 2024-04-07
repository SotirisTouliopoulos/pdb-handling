
class Parse:
    def __init__(self, PDBs):
        self.PDB = PDBs
        
    def coordinates(self):
        x = []
        y = []
        z = []
        with open(self.PDB) as file:
            for line in file:
                if line.startswith("ATOM"):
                    coord_x = line[30:38]
                    x.append(float(coord_x))

                    coord_y = line[38:46]
                    y.append(float(coord_y))

                    coord_z = line[46:54]
                    z.append(float(coord_z))
                
        print(x[0], y[0], z[0])
