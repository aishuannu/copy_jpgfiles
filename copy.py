import os
def copy(dirpath, file_extension, newdirpath):
    for root, dirname, files in os.walk(dirpath):
        for i in files:
            if i.endswith(file_extension):
                shutil.copy(os.path.join(root, i), os.path.join(newdirpath, i))
            
