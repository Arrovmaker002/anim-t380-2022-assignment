'''------------------Renaming frames with a specific naming convention and zipping up the result------------------'''


#Import Packages
import os
import sys

#dictionary for naming convention:
namingdict = {
    "project": "project name",
    "file": "file name",
    "frame": "frame number"
}



#print out results to a line
savedFileName = namingdict
print(savedFileName["project"]+"_"+savedFileName["file"]+"_"+savedFileName["frame"])