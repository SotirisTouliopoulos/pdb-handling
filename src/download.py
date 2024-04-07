
import wget
import sys

class Download:
    def __init__(self, PDBs, format, compression):
        self.PDBs = PDBs
        self.format = format
        self.compression = compression
        
        format = ["pdb","biounit"]
        if self.format not in format:
            print("Wrong format provided")
            sys.exit(1)

    def wget(self):        
        if self.format == "pdb":
            try:
                for file in self.PDBs:    
                    url = 'https://files.rcsb.org/download/' + file + '.pdb' + self.compression
                    wget.download(url)           
            except:
                print("Cannot download file: ", file)

        elif self.format == "biounit":
            try:
                for file in self.PDBs:    
                    url = 'https://files.rcsb.org/download/' + file + '.pdb1' + self.compression
                    wget.download(url)
            except:
                print("Cannot download file: ", file)
                
        else:
            pass

            