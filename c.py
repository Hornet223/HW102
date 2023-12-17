import os
import shutil
from_dir = r"C:\Users\sravy\Downloads"
to_dir = r"C:\Users\sravy\OneDrive\Desktop\Dowloaded Files"
# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx
# from_dir = "C:/Users/ADMIN/Downloads"
# to_dir = "C:/WhiteHatJr/dowanloadedimages"
 
list_of_files = os.listdir(from_dir)
 
for file_name in list_of_files:
 
    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
 
    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
 
        path1 = from_dir + '/' + file_name                         
        path2 = to_dir + '/' + "Image_Files"                     
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name   
        #print("path1 " , path1)
        #print("path3 ", path3)
 
        # Check if Folder/Directory Path Exists Before Moving
        # Else make a NEW Folder/Directory Then Move
        if os.path.exists(path2):
          print("Moving " + file_name + ".....")
 
          # Move from path1 ---> path3
          shutil.move(path1, path3)
 
        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)