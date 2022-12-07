import os
import bpy
from bpy.types import (Panel, Operator)

'''----------------------------------------- Baking full pbr functionality -----------------------------------------'''

#This code makes all selected objects snap to the cursor placement


# This is for allowing the code to be used as an addon for Blender
bl_info = {
    "name": "Move Selected Objects to World Origin",
    "author": "Vincent Arrouays, Brandon Jakosavic",
    "description": "Quickly move objects to cursor",
    "blender": (2, 80, 0),
    "location": "3D View",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~OPERATOINS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Move Cursor

class MoveCursorOperator(Operator):


    #Give the operation a name and label
    bl_idname = "object.movecursor_operator"
    bl_label = "Move Cursor to World Origin"

    #execute it the function
    def execute(self, context):
        
        #Move objects        
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                override = bpy.context.copy()
                override['area'] = area
                override['region'] = area.regions[4]
                
                
                #Move cursor to the world origin
                
                bpy.ops.view3d.snap_cursor_to_center()


        return {'FINISHED'}
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Move Objects 
    
class MoveObjectsOperator(Operator):


    #Give the operation a name and label
    bl_idname = "object.moveobjects_operator"
    bl_label = "Move Objects to Cursor"

    #execute it the function
    def execute(self, context):
        
        #Move objects        
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                override = bpy.context.copy()
                override['area'] = area
                override['region'] = area.regions[4]

                #Move objects in the world
                
                bpy.ops.view3d.snap_selected_to_cursor( override, use_offset=False)
        


        return {'FINISHED'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Panel~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Create a class for the Panel
class QuickUI(bpy.types.Panel):
    
    bl_idname = 'VIEW3D_PT_Cursor_panel'
    bl_label = 'Center Cursor and Objects'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    

    #Create a a UI by drawing, and calling the classes of the functions
    def draw(self, context):
        
        layout = self.layout

        col = layout.column(align=True)


        #Get each operation that will be used for the panel
        col.operator(MoveCursorOperator.bl_idname, text="Cursor to Origin", icon="PIVOT_CURSOR")
        col.operator(MoveObjectsOperator.bl_idname, text="Objects to Cursor", icon="STICKY_UVS_DISABLE")                  



# Register and Unregister the operations used in the panel

classes = (MoveCursorOperator, MoveObjectsOperator, QuickUI)

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