
# parse a text file with vina output

import os


def vina_score(vina_log):
    search = "   1"
    ligand_name = "Output will be"
    vina_log_file = open(vina_log, "r")
    lines = vina_log_file.readlines()
    for line in lines:
        if line.startswith(ligand_name):
            word = line.split()
            ligand = word[3]
    
        if line.startswith(search):
            word = line.split()
            score = word[1]
            print(score, ligand)
            
        


if __name__=="__main__":
    vina_score("vina_log.txt")

