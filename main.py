
from src.download import Download
from src.input import Input
import sys
import shutil


def major_flag(argv_list):
    flags = ["-d","-p","-h"]
    flag = []
    for argv in sys.argv:
        if argv in flags:
            flag.append(argv)

    if len(flag) == 1:
        flag = flag[0]
        return flag
    
    elif len(flag) > 1:
        print('Too many flags')
    else:
        print('Provide a flag')


def download_function(argv_list):
    
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
    
    try:
        shutil.rmtree("src/__pycache__")
    except:
        pass


def parse_function():
    pass


def call_function(flag):
    if flag == "-d":
        download_function(sys.argv)
    elif flag == "-p":
        pass
    
    
flag = major_flag(sys.argv)
call_function(flag)
