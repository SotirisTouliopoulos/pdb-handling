
from src.download import Download
from src.input import Input
import sys
import shutil

if '-d' in sys.argv:
    
    i_index = sys.argv.index('-i')
    
    try:
        comp_index = sys.argv.index('-comp')
        compression = 'gz'
    except:
        compression = ""

    input = sys.argv[i_index +1]
    format = sys.argv[i_index +2]
            
    input = Input(input)
    PDBs = input.get_input()

    structure = Download(PDBs , format, compression)
    structure.wget()
    
    shutil.rmtree("src/__pycache__")
                
elif '-p' in sys.argv:
    pass
