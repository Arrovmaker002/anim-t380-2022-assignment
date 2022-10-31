'''------------------Renaming frames with a specific naming convention and zipping up the result------------------'''


#Import Packages
import os
import sys
import shutil
import argparse

#dictionary for naming convention:
namingdict = {
    "project": "project name",
    "file": "file name",
    "frame": "frame number"
}


#print out dictionary results to a line
savedFileName = namingdict
print(savedFileName["project"]+"_"+savedFileName["file"]+"_"+savedFileName["frame"])

'''Copying files in a directory to another directory using shutil'''

source_input = input('Source folder: (type whole path name)')
destination_input = input('Destination folder: (type whole path name)')


source_folder = source_input+(r'\\')
destination_folder = destination_input+(r'\\')

""" copying files"""
# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # copy only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('copied', file_name)


