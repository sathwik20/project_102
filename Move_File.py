import os
import shutil
from importlib.resources import path

from_dir='C:/Users/admin/Downloads'
to_dir='C:/Users/admin/Documents'

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for key,value in list_of_files.items():
            name,extension=os.path.splitext(path) 
            if extension in value :
                file_name=os.path.basename(path)
                print('downloaded '+ file_name)
                path1=from_dir + '/' + file_name
                path2=to_dir + '/' + key
                path3=to_dir + '/' + key + '/' +file_name

            if os.path.exists(path2):
                   
                    print('moving' + file_name + '....')
                    shutil.move(path1,path3)
                   
            else:
                    
                    os.makedirs(path2)
                    print('moving' + file_name + '....')
                    shutil.move(path1,path3)
                   