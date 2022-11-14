'''------------------------------Create A Cube with  random color------------------------------'''

#import nessesary
import os
import bpy
from bpy.types import (Panel, Operator)

#This is for allowing the code to be used as an addon for Blender
bl_info = {
 "name": "Add Default Cube with random color",
 "author": "Vincent Arrouays",
 "description": "Creates a default Cube with a random color ",
 "blender": (3, 30, 1),
 "location": "3D View",
 "warning": "",
 "wiki_url": "",
 "tracker_url": "",
 "category": "Object"}

#add cube mesh to scene operation
class MeshOperator(Operator):


#Operation name and label
    bl_idname = "object.mesh_operator"
    bl_label = "Generate New Cube"

  bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))


#add color attribute to cube mesh generated