
from download import Download
from input import Input
import sys


if '-d' in sys.argv:
    
    d_index = sys.argv.index('-d')
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

    if sys.argv.index('--wget') == d_index +1:
        structure = Download(PDBs , format, compression)
        structure.wget()
        
    else:
        print("Please provide the method to download your file.\nExample: -d --wget")
        
elif '-p' in sys.argv:
    pass
