'''------------------Renaming frames with a specific naming convention requiring prompts from the user ------------------'''

#Import Packages
import os
import sys
import shutil
import zipfile
from zipfile import ZipFile
from os import path
from shutil import make_archive

#
#The naming convention demonstrated here goes the followin: 'project name'_'scene name'_'shot'_'version'_frame number
#We ask the values except the frame number (that will be generated automatically)


print("In the following Prompts, set the Project, scene")

projectName = input("Set Project name: ")
sceneName = input("Set Scene name: ")
shotName = input("Set Shot name: ")
shotVersion = input("Set Shot version: ")
imageFormat = input("Set Image format: ")

filename = f"{projectName}_{sceneName}_{shotName}_{shotVersion}_"

print(filename)

filesForRename_input = input('Folder with files to rename: ')

#iterate upon the files and rename them with correct numbering
os.chdir(filesForRename_input)
i=1
for file in os.listdir():
    src=file
    dst= filename + str(i) + imageFormat
    os.rename(src,dst)
    i+=1

