
import sys

class Input:
    def __init__(self, input):
        self.input = input
        
    def get_input(self):        
        PDBs = []
        if self.input[-4:] == ".txt":
            with open(self.input) as file:
                PDBs = []
                for line in file:
                    PDBs.append(line[:4])
            return PDBs

        elif len(self.input) == 4:
            PDBs.append(self.input)
            return PDBs