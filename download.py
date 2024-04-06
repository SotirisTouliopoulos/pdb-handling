
import ftplib
import sys


class Input:
    def __init__(self, input, format):
        self.input = input
        self.format = format
        
    def get_input(self):        
        PDBs = []
        if self.input[-4:] == ".txt":
            with open(self.input) as file:
                PDBs = []
                for line in file:
                    PDBs.append(line[:-1])
            return PDBs

        elif len(self.input) == 4:
            PDBs.append(self.input)
            return PDBs
            

class Download:
    def __init__(self, PDBs, format):
        self.input = PDBs
        self.format = format
        
    def ftp(self):
        try:
            ftp = ftplib.FTP("ftp.wwpdb.org")
        except:
            print('Unable to connect with PDB\n')
        finally:
            pass

        #log in
        try:
            ftp.login("anonymous", "password")
        except:
            print('Unable to log in with PDB\n')
        finally:
            pass


        if self.format == "biounit":
            try:
                path = '/pub/pdb/data/biounit/coordinates/all'
                ftp.cwd(path)
            except:
                print('Cannot access this PDB format\n')
            finally:
                pass 
            
            try:
                for pdb in self.input:
                    file = pdb + '.pdb1.gz'
                    ftp.retrbinary('RETR ' + file , open(file, 'wb').write)
            except:
                print('Failed to download this file\n')
            finally:
                pass

        
        elif self.format == "pdb":
            try:
                path = '/pub/pdb/data/structures/all/pdb'
                ftp.cwd(path)
            except:
                print('Cannot access this PDB format\n')
            finally:
                pass 

            try:
                for pdb in self.input:
                    file = 'pdb' + pdb + '.ent.gz'
                    ftp.retrbinary('RETR ' + file , open(file, 'wb').write)
            except:
                print('Failed to download this file\n')
            finally:
                pass

        ftp.quit()
            
        