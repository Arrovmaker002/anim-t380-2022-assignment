#Import nessesary packages for python
import os

'''-------------------------------- Create the Maya group with name ----------------------------------------'''
#Import maya packages
import maya.standalone
import maya.cmds as cmds



#____Initialise Maya
maya.standalone.initialize()

#____Create emty group with a name inside maya
cmds.group( em=True, name="Loli" )

#____save maya file as acii
cmds.file(rename=r"H:\Main Storage\College\Classes Current\Techincal Pipeline\anim-t380-2022-assignment\assignment - 3\asset\maya\scenes\Group.ma")
cmds.file(save=True, type="mayaAscii")
