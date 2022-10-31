'''------------------Renaming frames with a specific naming convention and zipping up the result------------------'''

#Import Packages
import os
import sys
import shutil
import zipfile
from zipfile import ZipFile
from os import path
from shutil import make_archive

#dictionary for naming convention:
namingdict = {
    "project": "project name",
    "file": "file name",
    "frame": "frame number"
}


#print out dictionary results to a line
savedFileName = namingdict
print(savedFileName["project"]+"_"+savedFileName["file"]+"_"+savedFileName["frame"])

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







"""______________________________Giving Option To Zip renamed files______________________________"""

#get input for if user wants a zip file
zip_option = input('Create ZIP? (Y/N)')

#variables for later
name_format = "ProjectName_shot"
zip_type = "A"
custom_zip_drc = '1'



#if user agrees ask user to specify a copy of the directory as zip or to zip up source
if zip_option == "Y" or zip_option == "y":
    print('Copy to ZIP file in same directory (A) or custom ZIP destination directory? (B) ')
    zip_type = input('A/B')
else:
    print('Files not Zipped.')
    quit()


#if user chose to zip and the zip type, do the zip function specified:
if zip_type == "A" or zip_type == "a":
    shutil.make_archive(source_folder + (r"\\")+name_format, 'zip', source_folder)
    print("Files Zipped")
else:
    custom_zip_drc = input('File path for custom ZIP destination directory: ')
    custom_zip_drc = custom_zip_drc +(r"\\")
    shutil.make_archive(custom_zip_drc+name_format, 'zip', source_folder)
    print("Files Zipped in "+custom_zip_drc)


