# pdb-handling
Tools to Download and Manipulate Protein Data Bank (PDB) files

Installation Guide

git clone https://github.com/SotirisTouliopoulos/pdb-handling.git

cd pdb-handling


Usage Guide

To download one PDB (1tii) format file:
python3 main.py -i 1tii pdb -d --wget

To download the biounit assembly format:
python3 main.py -i 1tii biounit -d --wget

To download multiple PDBs provide a ".txt" file including one of them in each line:
python3 main.py -i file.txt biounit -d --wget

To download the compressed version of PDBs add the "-comp" flag
python3 main.py -i file.txt biounit -d --wget -comp
