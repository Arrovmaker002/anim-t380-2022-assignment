
import argparse

parser = argparse.ArgumentParser(description='This script creates a bunch of cubes.')
parser.add_argument('num_cubes', type=int, help="Number of cubes")
args = parser.parse_args()

import maya.standalone
maya.standalone.initialize()
import maya.cmds

print("Creating {} cube(s)...".format(args.num_cubes))
for i in range(args.num_cubes):
    print("Created cube #{}".format(i))
    maya.cmds.polyCylinder()

print("Meshes in the Maya scene:")

print(maya.cmds.ls(geometry=True))