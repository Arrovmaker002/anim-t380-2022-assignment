'''------------------Renaming frames with a specific naming convention and zipping up the result------------------'''

#Import Packages
import os
import sys
import shutil
import zipfile
from zipfile import ZipFile
from os import path
from shutil import make_archive

print("___________Welcome to Frame Rename___________")
print("`````````````````````````````````````````````")
print("Set source and destination paths for files to edit")

print("In the following Prompts, set the Project, scene, and shot name as well as shot version and the desired image format (eg: .png")

projectName = input("Set Project name: ")
sceneName = input("Set Scene name: ")
shotName = input("Set Shot name: ")
shotVersion = input("Set Shot version: ")
#imageFormat = input("Set Image format: ")

"""______________________________Giving Option To Zip renamed files______________________________"""

#get input for if user wants a zip file
zip_option = input('Create ZIP? (Y/N)')




#if user agrees ask user to specify a copy of the directory as zip or to zip up source
if zip_option == "Y" or zip_option == "y":
    print('Copy to ZIP file in same directory (A) or custom ZIP destination directory? (B) ')
    zip_option = 'true'
    zip_type = input('A/B')
else:
    print('Files will not be Zipped.')


'''______________________________Copying files in a directory to another directory using shutil______________________________'''

source_input = input('Source folder: (type whole path name)')
destination_input = input('Destination folder: (type whole path name)')


source_folder = source_input+(r'\\')
destination_folder = destination_input+(r'\\')

"""______________________________Copying files______________________________"""
# fetch all files from the source directory and copy them to the destination directory
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # copy only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('copied', file_name)

#The naming convention demonstrated here goes the followin: 'project name'_'scene name'_'shot'_'version'_frame number
#We ask the values except the frame number (that will be generated automatically)




filename = f"{projectName}_{sceneName}_{shotName}_{shotVersion}_"


filesForRename_input = destination_input

name_format = filename

#iterate upon the files and rename them with correct numbering
os.chdir(filesForRename_input)
i=1
for file in os.listdir():
    src=file
    dst= filename + str(i) + ".png"
    os.rename(src,dst)
    i+=1




#variables for zipping
zip_type = "A"
custom_zip_drc = '1'
#changing to correct source folder for file zipping to use
source_folder = destination_folder

#if user chose to zip and the zip type, do the zip function specified:
if zip_type == "A" or zip_type == "a" and zip_option == "true":
    shutil.make_archive(source_folder + (r"\\") + name_format, 'zip', source_folder)
    print("Files Zipped")
elif zip_type == "B" or zip_type == "b" and zip_option == "true":
    custom_zip_drc = input('File path for custom ZIP destination directory: ')
    custom_zip_drc = custom_zip_drc + (r"\\")
    shutil.make_archive(custom_zip_drc + name_format, 'zip', source_folder)
    print("Files Zipped in " + custom_zip_drc)
else:
    quit()


