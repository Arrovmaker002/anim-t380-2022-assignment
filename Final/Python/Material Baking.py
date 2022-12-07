'''----------------------------------------- Baking full pbr functionality -----------------------------------------'''
# importing necessary packages
import os
import bpy
from bpy.types import (Panel, Operator)

# This is for allowing the code to be used as an addon for Blender
bl_info = {
    "name": "Simple PBR Baker",
    "author": "Vincent Arrouays, Brandon Jakosavic",
    "description": "Quickly bakes a material to  PBR texture set",
    "blender": (2, 80, 0),
    "location": "3D View",
    "warning": "In Development",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"}


obj = bpy.context.active_object
# Set a default name and Texture size
image_name = obj.name + '_BakedTexture'


img = bpy.data.images.new(image_name,1024,1024)

#Since there are multiple material, we need to iterate on the materials to assign them to
# the correct maps   

for mat in obj.data.materials:

    mat.use_nodes = True 
    #Because this was made with node we say its true
    nodes = mat.node_tree.nodes
    texture_node =nodes.new('ShaderNodeTexImage')
    texture_node.name = 'Bake_node'
    texture_node.select = True
    nodes.active = texture_node
    
#Assign an image to the node
    
    texture_node.image = img

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PANELS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ColorMap

#Define class for Recalculating Normals
class BakeColorMapOperator(Operator):


    #Give the operation a name and label
    bl_idname = "object.color_operator"
    bl_label = "Bake Color Map"

    #execute it the function
    def execute(self, context):
        
        #Bake Color    
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.bake(type='DIFFUSE', save_mode='EXTERNAL')
        img.save_render(filepath='C:\\Textures\\ColorMap_baked.png')

        return {'FINISHED'}
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RoughnessMap

#Define class for Recalculating Normals
class BakeRoughnessMapOperator(Operator):


    #Give the operation a name and label
    bl_idname = "object.roughness_operator"
    bl_label = "Bake Roughness Map"

    #execute it the function
    def execute(self, context):
        
        #Bake Roughness
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.bake(type='ROUGHNESS', save_mode='EXTERNAL')
        img.save_render(filepath='C:\\Textures\\RoughnessMap_baked.png')

        return {'FINISHED'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~NormalMap

#Define class for Recalculating Normals
class BakeNormalMapOperator(Operator):


    #Give the operation a name and label
    bl_idname = "object.normal_operator"
    bl_label = "Bake Normal Map"

    #execute it the function
    def execute(self, context):
        
        #Bake Normal
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.bake(type='NORMAL', save_mode='EXTERNAL')
        img.save_render(filepath='C:\\Textures\\NormalMap_baked.png')

        return {'FINISHED'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EmissionMap

#Define class for Recalculating Normals
class BakeEmissionMapOperator(Operator):


    #Give the operation a name and label
    bl_idname = "object.emission_operator"
    bl_label = "Bake Emission Map"

    #execute it the function
    def execute(self, context):

        #Bake Emission
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.bake(type='EMIT', save_mode='EXTERNAL')
        img.save_render(filepath='C:\\Textures\\Emission_baked.png')        

        return {'FINISHED'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~AmbientOcclusionMap

#Define class for Recalculating Normals
class BakeAoMapOperator(Operator):


    #Give the operation a name and label
    bl_idname = "object.ao_operator"
    bl_label = "Bake AO Map"

    #execute it the function
    def execute(self, context):
        
        #Bake Ambient Occlusion
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.bake(type='AO', save_mode='EXTERNAL')
        img.save_render(filepath='C:\\Textures\\AO_baked.png')

        return {'FINISHED'}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Bake All Maps

#Define class for Recalculating Normals
class BakeAllOperator(Operator):


    #Give the operation a name and label
    bl_idname = "object.all_operator"
    bl_label = "Bake All Maps"

    #execute it the function
    def execute(self, context):
        
        #Bake Ambient Occlusion
        bpy.context.view_layer.objects.active = obj
        
        bpy.ops.object.bake(type='DIFFUSE', save_mode='EXTERNAL')
        img.save_render(filepath='C:\\Textures\\ColorMap_baked.png')
        
        bpy.ops.object.bake(type='ROUGHNESS', save_mode='EXTERNAL')
        img.save_render(filepath='C:\\Textures\\RoughnessMap_baked.png')        
        
        bpy.ops.object.bake(type='NORMAL', save_mode='EXTERNAL')
        img.save_render(filepath='C:\\Textures\\NormalMap_baked.png')

        bpy.ops.object.bake(type='EMIT', save_mode='EXTERNAL')
        img.save_render(filepath='C:\\Textures\\Emission_baked.png')   
        
        bpy.ops.object.bake(type='AO', save_mode='EXTERNAL')
        img.save_render(filepath='C:\\Textures\\AO_baked.png')        

        return {'FINISHED'}



    
#In the last step, we are going to delete the nodes we created earlier
#for mat in obj.data.materials:
#    for n in mat.node_tree.nodes:
#        if n.name == 'Bake_node':
#           mat.node_tree.nodes.remove(n)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Panel~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Create a class for the Panel
class BakingUI(bpy.types.Panel):
    
    bl_idname = 'VIEW3D_PT_Baking_panel'
    bl_label = 'Bake Textures'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    

    #Create a a UI by drawing, and calling the classes of the functions
    def draw(self, context):
        
        layout = self.layout

        col = layout.column(align=True)


        #Get each operation that will be used for the panel
        col.operator(BakeColorMapOperator.bl_idname, text="Bake Color Map")        
        col.operator(BakeRoughnessMapOperator.bl_idname, text="Bake Roughness Map")        
        col.operator(BakeNormalMapOperator.bl_idname, text="Bake Normal Map")        
        col.operator(BakeEmissionMapOperator.bl_idname, text="Bake Emission Map")
        col.operator(BakeAoMapOperator.bl_idname, text="Bake AO Map")        
        col.operator(BakeAllOperator.bl_idname, text="Bake All Maps")                    



# Register and Unregister the operations used in the panel

classes = (BakeColorMapOperator, BakeRoughnessMapOperator, BakeNormalMapOperator, BakeEmissionMapOperator, BakeAoMapOperator, BakeAllOperator, BakingUI)

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
