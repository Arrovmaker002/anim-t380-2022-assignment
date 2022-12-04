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

classes = (BakeryOperator, QuickUI)

class BakeryOperation(bpy.types.Operator):
    bl_idname = "bakery.bake"
    bl_label = "Bake textures"

    def invoke(self, context, event):
        scn = context.scene
        materials = set()
        for o in scn.bake_objects:
            materials = materials.union(set(map(lambda x: (o.name, x.name), bpy.data.objects[o.name].data.materials)))

        for (name, material) in materials:
            bpy.data.materials[material].use_nodes = True
            node_tree = bpy.data.materials[material].node_tree
            found = False

            img_name = name+"_bake"
            for n in [n for n in node_tree.nodes if n.type == 'TEX_IMAGE']:
                found = False

                if n.image != None and n.image.name == img_name:
                    n.select = True
                    node_tree.nodes.active = n
                    found = True
                    break
            if not found:
                node = node_tree.nodes.new("ShaderNodeTexImage")
                node.select = True
                node_tree.nodes.active = node
                if img_name in bpy.data.images:
                    node.image = bpy.data.images[img_name]
                else:
                    node.image = bpy.data.images.new(name + "_bake", 512, 512)

            img = bpy.data.images[img_name]

            bpy.ops.object.select_all("EXEC_DEFAULT", action="DESELECT")
            bpy.ops.object.select_pattern(pattern = name)
            bpy.context.scene.objects.active = bpy.data.objects[name]
            bpy.ops.uv.lightmap_pack("EXEC_SCREEN")
            print("Baking " + name)
            bpy.ops.object.bake("INVOKE_DEFAULT") # or EXEC_DEFAULT
        return {'FINISHED'}


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
