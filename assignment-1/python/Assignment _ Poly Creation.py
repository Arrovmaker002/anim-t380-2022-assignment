
#import required:
import argparse
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds

"""This a docstring"""
#this is a comment
#set up arguemnt parser for user input
parser = argparse.ArgumentParser(description='This script creates a bunch of cylinders.')
parser.add_argument('num_cylinders', type=int, help="Number of cylinders")
args = parser.parse_args()

#ask for the user input and create the number of objects required
print("Enter the number to Creating {} cylinder(s)...".format(args.num_cylinders))
for i in range(args.num_cylinders):
    print("Created cylinders #{}".format(i))
    maya.cmds.polyCylinder()

#print output to console with number of cubes created
print("Meshes in the Maya scene:")
print(maya.cmds.ls(geometry=True))

#save maya file as acii
cmds.file(rename="H:\Main Storage\College\Classes Current\Techincal Pipeline/anim-t380-2022-assignment/assignment-1\objects.ma")
cmds.file(save=True, type="mayaAscii")


#close maya in the background after process is done
maya.standalone.uninitialize()