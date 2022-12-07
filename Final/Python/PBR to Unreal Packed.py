'''----------------------------------------- Baking full pbr functionality -----------------------------------------'''
# importing necessary packages
import os
import bpy
from bpy.types import (Panel, Operator)

# This is for allowing the code to be used as an addon for Blender
bl_info = {
    "name": "PBR to Packed Converter",
    "author": "Vincent Arrouays, Brandon Jakosavic",
    "description": "Generates a setup to combine AO, Mettalic and Roughness map into a single map for Unreal / other game engines",
    "blender": (3, 30, 0),
    "location": "3D View",
    "warning": "In Development",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"}




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PANELS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#----------------------------------Set up converter material and Plane

#Define class for getting converter material

class SetupConvertOperator(Operator):


    # Give the operation a name and label
    bl_idname = "object.converter_operator"
    bl_label = "Setup Converter"


    def execute(self, context):

        #read from blender file and load necessary objects
        file_path = r'H:\Main Storage\College\Classes Current\Techincal Pipeline\anim-t380-2022-assignment\Final\Asset\Converter_Setup.blend'
        inner_path = 'Object'
        object_name = 'ConvertBakePlane'
        bpy.ops.wm.append(filepath = os.path.join(file_path, inner_path, object_name), directory = os.path.join(file_path, inner_path), filename = object_name)

        return {'FINISHED'}





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Bake All Maps

#Define class for Baking the ARM Map:
class BakeARMOperator(Operator):


    #Give the operation a name and label
    bl_idname = "object.bake_operator"
    bl_label = "Bake ARM Map"

    #execute the function
    def execute(self, context):
        obj = bpy.context.active_object
        # Set a default name and Texture size
        image_name = obj.name + 'ARM_BakedTexture'

        img = bpy.data.images.new(image_name, 1024, 1024)

        # Since there are multiple material, we need to iterate on the materials to assign them to
        # the correct maps

        for mat in obj.data.materials:
            mat.use_nodes = True
            # Because this was made with node we say its true
            nodes = mat.node_tree.nodes
            texture_node = nodes.new('ShaderNodeTexImage')
            texture_node.name = 'Bake_node'
            texture_node.select = True
            nodes.active = texture_node

            # Assign an image to the node

            texture_node.image = img

        #Bake ARM

        bpy.context.view_layer.objects.active = obj

        bpy.ops.object.bake(type='DIFFUSE', save_mode='EXTERNAL')
        img.save_render(filepath= r'C:\Users\vince\Downloads\ARMMap_baked.png')


        return {'FINISHED'}




#In the last step, we are going to delete the nodes we created earlier
#for mat in obj.data.materials:
#    for n in mat.node_tree.nodes:
#        if n.name == 'Bake_node':
#           mat.node_tree.nodes.remove(n)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Panel~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Create a class for the Panel
class QuickUI(bpy.types.Panel):

    bl_idname = 'VIEW3D_PT_T_panel'
    bl_label = 'Convert and Bake ARM Texture'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'


    #Create a a UI by drawing, and calling the classes of the functions
    def draw(self, context):

        layout = self.layout

        col = layout.column(align=True)


        #Get each operation that will be used for the panel
        col.operator(SetupConvertOperator.bl_idname, text="Setup Convert Objects", icon="DOWNARROW_HLT")
        col.operator(BakeARMOperator.bl_idname, text="Bake ARM Map", icon="RENDER_RESULT")




# Register and Unregister the operations used in the panel

classes = (SetupConvertOperator, BakeARMOperator, QuickUI)

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
