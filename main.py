
from src.download import Download
from src.input import Input
import sys
import shutil


def major_flag(argv_list):
    major_flag = []
    for argv in sys.argv:
        if len(argv) == 2 and argv[0] == '-':
            major_flag.append(argv)

    if len(major_flag) == 2:
        major_flag.remove('-i')
        #major_flag.remove('-o')
        flag = major_flag[0]
        return flag
    
    elif len(major_flag) > 2:
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
    
    shutil.rmtree("src/__pycache__")


def parse_function():
    pass


def call_function(flag):
    if flag == "-d":
        download_function(sys.argv)
    elif flag == "-p":
        pass
    
    
flag = major_flag(sys.argv)
call_function(flag)
