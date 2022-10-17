'''------------------Incremental Save Script using Mel Commands------------------'''

#Import Packages
import maya.cmds as cmds
import os
import sys

#Running the Mel command
def runincrementalSaveScene():
    mel.eval("incrementalSaveScene;")
runincrementalSaveScene()

#Printing out result
print("Scene Increment Saved and Opened!")