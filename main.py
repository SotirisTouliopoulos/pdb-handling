
from download import Download
from input import Input
import sys


input = sys.argv[1]
format = sys.argv[2]
compression = sys.argv[3]


input = Input(input)
PDBs = input.get_input()


structure = Download(PDBs , format, compression)
#structure.ftp()
structure.wget()
