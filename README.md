This contains python code to collect a copy of files into another folder with specific extension from a folder.


dirpath - give the directory path from which you want to collect a copy of files.
file_extenstion - give the extension of files you want to collect(eg. ".jpg" or ".py").
newdirpath - give the directory path to which you want to copy the files.

If you replace "shutil.copy()" by "shutil.move()" in the code , it will move the files into another folder instead of collecting a copy of files. This will help when we want to collect all the files with specific extension and put them in a new folder.
