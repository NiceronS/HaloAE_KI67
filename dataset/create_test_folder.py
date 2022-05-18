"""
Puisque nous n'avons pas l'equivalent de la database de MVTec avec un dossier test contenant deux sous dossier par object, avec un label good, et un autre != de good, on va 
cree ce truc la faisant un scripte de copy paste des images que emilie a regroupe par patient. 
"""
import os
import shutil

path_data = '/data/lungNENomics/work/MathianE/KI67_Normal_Tumoral'

path_test = '/home/nicerons/Documents/test'

list_patient = os.listdir(path_data) 
for patient in list_patient:
    p_patient = os.path.join(path_data, patient)
    label_list = os.listdir(p_patient)
    for label in label_list:
        p_label = os.path.join(path_data,patient,label)
        list_img = os.listdir(p_label)
        print(label)
        if label == 'Normal':
            copy_path = os.path.join(path_test, 'Normal')
        else :
            copy_path = os.path.join(path_test, 'Tumor')
        for img in list_img:
            p_img = os.path.join(path_data,patient,label,img)
            shutil.copy(p_img,copy_path)

if len(os.listdir(copy_path) ) == 0:
    print("Directory is empty")
else:    
    print("Directory is not empty")

