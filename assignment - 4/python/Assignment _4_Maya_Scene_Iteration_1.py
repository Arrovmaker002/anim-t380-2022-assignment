'''-------------------------------- Save a copy of the scene with increment naming format ----------------------------------------'''
#Import Nessesary packages

import maya.cmds as cmds
import os
import sys

#finding the name and path of the
fullName = cmds.file( q = 1, sn = 1, shn =1)
SceneName = cmds.file()
fullNamePath = cmds.file( q = 1, sn = 1)
PathName = os.path.dirname(fullNamePath)

#Printing Path Name for debug and status
print(PathName)


#Function that adds to the number for the new version of the scene by opening a cache file that has the number of the last iteration stored

f = open(f"{PathName}/iteration_cache/scene_iteration_cache.txt", "w")
lastVersion = f.read()

#Math to add to the version count
currentVersion = lastVersion + 1

#---writes the new version count and closes the file
f.write(currentVersion)
f.close()


#____save maya file as acii with naming convention
cmds.file(rename=f"{PathName}/{SceneName}.{currentVersion}.ma")
cmds.file(save=True, type="mayaAscii")

