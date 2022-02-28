import os




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
    #structure(dlg_file)
            

def structure(dlg_file, number=5):
    
    fhandle = open(dlg_file,encoding='utf-8')
    lines = fhandle.readlines()

    all_conformers = []
    i = 1
    for line in lines:
    
        if line.startswith("DOCKED: ATOM"):
            all_conformers.append(line)


        if line.startswith("DOCKED: ENDMDL"):
            all_conformers.append(line)

            if i != number:
                all_conformers = []
            
            if i == number:
                with open('conf.pdbqt', 'x') as f:
                    for item in all_conformers:
                        f.write("%s" % item)
                break

            i = i + 1



        if i > number:
            break
        

parse_it("/run/media/karthi/SOFT/Docking/Hari/2v55/")