import os
import shutil


os.mkdir("image_folder",exist_ok=True)
os.mkdir("text_folder",exist_ok=True)
os.mkdir("pdf_folder",exist_ok=True)


for filename in os.listdir():
    path=os.path.join(r"C:\Users\vanshika\Desktop\JECRC",filename)

    if filename.endswith(".png"):
        shutil.move(path,"image_folder")
        print(f"moved{filename} to image_folder")

    elif filename.endswith(".txt"):
        shutil.move(path,"text_folder")
        print(f"moved{filename} to text_folder")
    
    elif filename.endswith(".pdf"):
        shutil.move(path,"pdf_folder")
        print(f"moved{filename} to pdf_folder")




