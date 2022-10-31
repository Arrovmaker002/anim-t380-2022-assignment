'''------------------Renaming frames with a specific naming convention requiring prompts from the user ------------------'''

#Import Packages
import os
import sys
import shutil
import zipfile
from zipfile import ZipFile
from os import path
from shutil import make_archive


#The naming convention demonstrated here goes the followin: 'project name'_'scene name'_'shot'_'version'_frame number
#We ask the