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

    texture_node.image = im

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PANELS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ColorMap Baking

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




metal = cv2.imread(input('path to metal texture:'))


metalb, metalg, metalr = cv2.imsplit(metal)

imgshow('metalb', metalb]



final = cv2.merge(metalb, occlusingg, roughnessr)

final = cv2.write('ARM texture'+ .png)