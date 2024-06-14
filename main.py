import os, shutil

path = r"C:/Users/jonat/Downloads/"

file_name = os.listdir(path);

folder_names = ["ZIP", "PDF", "DOCX", "PNG", "EXE", "PPTX"]

for loop in range(0,5):
    if not (os.path.exists(path+folder_names[loop])):
        os.makedirs(path+folder_names[loop])


for file in file_name:
    if(".zip" in file and not os.path.exists(path+"ZIP/" + file)):
        shutil.move(path+file, path+"ZIP/" + file)
    elif(".docx" in file and not os.path.exists(path+"DOCX/" + file)):
        shutil.move(path+file, path+"DOCX/" + file)
    elif(".exe" in file and not os.path.exists(path+"EXE/" + file)):
        shutil.move(path+file, path+"EXE/" + file)
    elif(".pdf" in file and not os.path.exists(path+"PDF/" + file)):
        shutil.move(path+file, path+"PDF/" + file)
    elif(".png" in file and not os.path.exists(path+"png/" + file)):
        shutil.move(path+file, path+"PNG/" + file)
    elif(".PNG" in file and not os.path.exists(path+"png/" + file)):
        shutil.move(path+file, path+"PNG/" + file)
    else:
        print("There are files in this path that were not moved!")
