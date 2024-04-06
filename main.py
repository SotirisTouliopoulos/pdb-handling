
from download import Download, Input
import sys


input = Input( sys.argv[1] , sys.argv[2] )
PDBs = input.get_input()


structure = Download(PDBs , sys.argv[2])
structure.ftp()

