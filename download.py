
import ftplib
import sys
import wget
         

class Download:
    def __init__(self, PDBs, format, compression):
        self.PDBs = PDBs
        self.format = format
        self.compression = compression
        
    def ftp(self):
        
        print("Please note that the FTP protocol will be phased out on November 1st 2024\n")
        
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
                for pdb in self.PDBs:
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
                for pdb in self.PDBs:
                    file = 'pdb' + pdb + '.ent.gz'
                    ftp.retrbinary('RETR ' + file , open(file, 'wb').write)
            except:
                print('Failed to download this file\n')
            finally:
                pass

        ftp.quit()
        

    def wget(self):        
        if self.format == "pdb":
            try:
                for file in self.PDBs:    
                    url = 'https://files.rcsb.org/download/' + file + '.pdb' + self.compression
                    wget.download(url)
            
            except:
                print("Cannot download this file")