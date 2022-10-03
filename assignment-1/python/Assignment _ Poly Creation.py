

import argparse
import maya.standalone
maya.standalone.initialize()
import maya.cmds

"""This a docstring"""
#this is a comment
parser = argparse.ArgumentParser(description='This script creates a bunch of cylinders.')
parser.add_argument('num_cylinders', type=int, help="Number of cylinders")
args = parser.parse_args()


print("Enter the number to Creating {} cylinder(s)...".format(args.num_cylinders))
for i in range(args.num_cylinders):
    print("Created cylinders #{}".format(i))
    maya.cmds.polyCylinder()

print("Meshes in the Maya scene:")
print(maya.cmds.ls(geometry=True))

#close maya in the background after process is done
maya.standalone.uninitialize()