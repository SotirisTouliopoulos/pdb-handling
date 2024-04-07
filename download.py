
import sys
import wget
         

class Download:
    def __init__(self, PDBs, format, compression):
        self.PDBs = PDBs
        self.format = format
        self.compression = compression

    def wget(self):        
        if self.format == "pdb":
            try:
                for file in self.PDBs:    
                    url = 'https://files.rcsb.org/download/' + file + '.pdb' + self.compression
                    wget.download(url)           
            except:
                print("Cannot download this file")

                
        if self.format == "biounit":
            try:
                for file in self.PDBs:    
                    url = 'https://files.rcsb.org/download/' + file + '.pdb1' + self.compression
                    wget.download(url)
            except:
                print("Cannot download this file")

            