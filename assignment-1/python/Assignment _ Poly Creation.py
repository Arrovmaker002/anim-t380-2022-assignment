

import argparse
parser = argparse.ArgumentParser(description='This script creates a bunch of cylinders.')
parser.add_argument('num_cubes', type=int, help="Number of cubes")
args = parser.parse_args()

import maya.standalone
maya.standalone.initialize()
import maya.cmds

print("Creating {} cube(s)...".format(args.num_cylinders))
for i in range(args.num_cylinders):
    print("Created cylinders #{}".format(i))
    maya.cmds.polyCylinder()

print("Meshes in the Maya scene:")
print(maya.cmds.ls(geometry=True))

maya.standalone.initialize()