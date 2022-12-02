'''----------------------------------------- PBR to Unreal Packed functionality -----------------------------------------'''

# importing necessary packages
import os
import bpy
from bpy.types import (Panel, Operator)

# This is for allowing the code to be used as an addon for Blender
bl_info = {
    "name": "PBR to Unreal Packed",
    "author": "Vincent Arrouays, Brandon Jakosavic",
    "description": "Converts a PBR texture set to a Unreal Packed Texture set within Blender",
    "blender": (3, 30, 1),
    "location": "3D View",
    "warning": "In Development",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"}



# Register and Unregister the operations used in the panel (code from Brandon Jakovasic)

classes = (MeshOperator, QuickUI)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

if __name__ == "__main__":
    register()
