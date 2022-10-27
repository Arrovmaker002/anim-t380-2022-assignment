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



#copying files in a directory using shutil

source_folder = r"H:\Main Storage\College\Classes Current\Techincal Pipeline\anim-t380-2022-assignment\Midterm\asset\Techincal Pipeline Midterm\\"
destination_folder = r"H:\Main Storage\College\Classes Current\Techincal Pipeline\anim-t380-2022-assignment\Midterm\asset\outgoing assets\\"
