'''Give option to zip'''
#importing a lot of stuff
import os
import sys
import shutil
import pathlib
import zipfile
from zipfile import ZipFile
from os import path
from shutil import make_archive

#get input for if user wants a zip file
zip_option = input('Create ZIP? (Y/N)')

#variables for later
name_format = "ProjectName_shot"
zip_type = "A"
custom_zip_drc = '1'
source_folder = r"H:\Main Storage\College\Classes Current\Techincal Pipeline\anim-t380-2022-assignment\Midterm\asset\Techincal Pipeline Midterm\images"


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
