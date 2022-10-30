#import nessesary python packages
import os
import sys
import shutil

#copying files in a directory using shutil

source_folder = r"H:\Main Storage\College\Classes Current\Techincal Pipeline\anim-t380-2022-assignment\Midterm\asset\Techincal Pipeline Midterm\images\\"
destination_folder = r"H:\Main Storage\College\Classes Current\Techincal Pipeline\anim-t380-2022-assignment\Midterm\asset\outgoing assets\\"

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