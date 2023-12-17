import os
import shutil
from_dir = r"C:\Users\sravy\Downloads"
to_dir = r"C:\Users\sravy\OneDrive\Desktop\Dowloaded Files"
list_of_files = os.listdir(from_dir)
# print(list_of_files)
for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)
    print(name)
    print(ext)
    if ext == "":
        continue
    if ext in [".gif", ".png", "jpg", "jpeg", "jfif"]:
        path1 = from_dir + "/" + file_name
        path2 = from_dir + "/" + "Image_Files"
        path3 = to_dir + "/" + "Image_Files" + "/" + file_name
        print("path1", path1)
        print("path3", path3)
        if os.path.exists(path2):
            print("Moving " + file_name + "....")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + "....")
            shutil.move(path1, path3)
