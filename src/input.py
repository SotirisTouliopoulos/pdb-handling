
import sys

class Input:
    def __init__(self, input):
        self.input = input
        
    def get_input(self):        
        PDBs = []
        
        # for download
        if self.input[-4:] == ".txt":
            with open(self.input) as file:
                PDBs = []
                for line in file:
                    PDBs.append(line[:4])
            return PDBs

        elif len(self.input) == 4:
            PDBs.append(self.input)
            return PDBs
        
        # for parse
        elif self.input[-4:] == ".pdb" or self.input[-5:] == ".pdb1":
            PDBs.append(self.input)
            PDBs = PDBs[0]
            return PDBs
         