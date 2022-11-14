'''------------------------------Create A Cube with  random color------------------------------'''

# import necessary packages
import os
import bpy
from bpy.types import (Panel, Operator)
import random

# This is for allowing the code to be used as an addon for Blender
bl_info = {
    "name": "Add a default cube with random color",
    "author": "Vincent Arrouays",
    "description": "Creates a default Cube with a random color ",
    "blender": (3, 30, 1),
    "location": "3D View",
    "warning": "Very fun.",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"}


# Material creation code (to be called later)(code from Vividfax)
# New material
def newMaterial(id):
    mat = bpy.data.materials.get(id)

    if mat is None:
        mat = bpy.data.materials.new(name=id)
    mat.use_nodes = True
    if mat.node_tree:
        mat.node_tree.links.clear()
        mat.node_tree.nodes.clear()
    return mat
# Add Shaders within the material
def newShader(id, type, r, g, b):
    mat = newMaterial(id)

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    output = nodes.new(type='ShaderNodeOutputMaterial')
    if type == "diffuse":
        shader = nodes.new(type='ShaderNodeBsdfDiffuse')
        nodes["Diffuse BSDF"].inputs[0].default_value = (r, g, b, 1)
    elif type == "emission":
        shader = nodes.new(type='ShaderNodeEmission')
        nodes["Emission"].inputs[0].default_value = (r, g, b, 1)
        nodes["Emission"].inputs[1].default_value = 1
    elif type == "glossy":
        shader = nodes.new(type='ShaderNodeBsdfGlossy')
        nodes["Glossy BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glossy BSDF"].inputs[1].default_value = 0
    links.new(shader.outputs[0], output.inputs[0])
    return mat

'''# Generate the random numbers for the r, g, b values
r = random.uniform(0, 1)
g = random.uniform(0, 1)
b = random.uniform(0, 1)
'''
# Mesh Operation Code
class MeshOperator(Operator):
    # Operation name and label
    bl_idname = "object.mesh_operator"
    bl_label = "Generate New Cube"

    # Execute it the function
    def execute(self, context):
        # Create new material with shader
        mat = newShader("Random Cube Color", "diffuse", random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        # Command to add the cube
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        # Add shader to the cube
        bpy.context.active_object.data.materials.append(mat)

        return {'FINISHED'}


# UI code
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
