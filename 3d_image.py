import os
from pymol import cmd
# dlg parser and 3d images generation 
#provide main docking folder


def save_image(file):
    base_name = file.split("\\")[-2]
    cmd.load (file)
    cmd.extract("ligand", "organic")
    cmd.show("surface", "result")
    cmd.util.chainbow("result")
    cmd.hide("surface", "organic")
    cmd.show("sticks", "organic")
    cmd.orient()
    print(base_name + ".png")
    cmd.ray(1028,768)
    cmd.png(base_name + ".png", width=1024, height=768, dpi=300, ray=1)
    cmd.delete("*")


def get_file(docking_folder):
    folders = os.listdir(docking_folder)
    for eachfolder in folders:
        sub_folder = os.path.join(docking_folder, eachfolder)
        if os.path.isdir(sub_folder):
            pdbqt_files = os.listdir(sub_folder)
            for eachfile in pdbqt_files:
                if eachfile.endswith(".pdbqt") and eachfile.startswith("result"):
                    pdbqt_file = os.path.join(sub_folder, eachfile)
                    save_image(pdbqt_file)
                    

def parse_it(fol):
    searc = "DOCKED: USER    Estimated Free Energy of Binding"
    main_folder = fol

    
    dlg_files = []

    if str(fol).endswith(".dlg"):
        score(fol)

    if os.path.isdir(main_folder) == False:
        print(main_folder, "-", "This is not valid directory")
        quit()

    folder_list = os.listdir(main_folder)
    for eachfolder in folder_list:
        if os.path.isdir(os.path.join(main_folder, eachfolder)) == True:
            if os.path.exists(os.path.join(main_folder, eachfolder, "dock.dlg")):
                dlg_files.append(os.path.join(main_folder, eachfolder, "dock.dlg"))
    
    for eachfolder in folder_list:
        if str(os.path.join(main_folder, eachfolder)).endswith(".dlg"):
            dlg_files.append(os.path.join(main_folder, eachfolder))
    

    for file in dlg_files:
        score(file)
    

def score(dlg_file):
    
    searc = "DOCKED: USER    Estimated Free Energy of Binding"
    fhandle = open(dlg_file,encoding='utf-8')
    lines = fhandle.readlines()
    conf_score = []
    for line in lines:
        if line.startswith(searc):
            word = line.split()
            score = word[8]
            #list = score.split(sep = "-")
            #number = list[1]
            number = float(score)
            conf_score.append(number)
    conf_score.sort()
    if len(conf_score) == 0:
        print("No score", dlg_file)
    if not len(conf_score) == 0:
        best_conf = conf_score[0]
        print(best_conf, dlg_file)
    structure(dlg_file)
            

def structure(dlg_file):
   

   pass

docking_folder = "/home/karthi/Desktop/KKS/4fa6/ligands/COMPOUND_C/"
os.chdir(docking_folder)
#parse dock.dlg file to get scores
parse_it(docking_folder)

#get 3d images of docking poses
ans = input("Do you want docked pose 3D images Y/N")
if ans == "Y" or "y":
    get_file(docking_folder)
    print("Done")
else:
    print("Done")
