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

#execute it the function
    def execute(self, context):

        #command to add the cube
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

        return {'FINISHED'}

#add color attribute to cube mesh generated (WIP)

#UI code
class QuickUI(bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_example_panel'
    bl_label = 'Random Colored Cube Generation'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    # Create a UI:
    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)

        # Get each operation that will be used for the panel
        col.operator(MeshOperator.bl_idname, text="Generate Cube", icon="MESH_CUBE")


#Register and Unregister the operations used in the panel (code from Brandon Jakovasic)

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