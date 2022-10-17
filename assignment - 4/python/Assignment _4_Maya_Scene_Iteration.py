#Import nessesary packages for python
import os


#Finds the root path of the project




#opens the .txt file and reads whats inside it for the current save number
file = open(r"H:\Main Storage\College\Classes Current\Techincal Pipeline\anim-t380-2022-assignment\assignment - 3\etc/asset.alias")

saveNumber = file.read()


'''-------------------------------- Create the Maya group with name ----------------------------------------'''
#Import maya packages

import maya.cmds as cmds
import os
import sys




#____Function that adds to teh number after each activation of the script
cmds.group( em=True, name=groupname )

version = 0+

"C:mayscenes/scene/scene"[version]



#____save maya file as acii
cmds.file(rename=r"H:\Main Storage\College\Classes Current\Techincal Pipeline\anim-t380-2022-assignment\assignment - 3\asset\maya\scenes\Group.ma")
cmds.file(save=True, type="mayaAscii")

#____Uninitialize Maya (just in case)
maya.standalone.uninitialize()