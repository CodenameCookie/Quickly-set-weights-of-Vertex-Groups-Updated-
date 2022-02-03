bl_info = {
    "name": "Quickly set weights of Vertex Groups",
    "author": "nicmar",
    "version": (1, 0),
    "blender": (2, 78, 0),
    "location": "Properties Editor > Object data > Vertex Groups",
    "description": "Quickly set Vertex Groups with assigned weight and live edit",
    "warning": "",
    "wiki_url": "",
    "category": "Mesh"}

import bpy
import time
from bpy.types import Panel

class PANEL1_PT_QuickWeightPanel(bpy.types.Panel):
    bl_label = "Quick Vertex Weights"
    bl_space_type = "PROPERTIES";
    bl_region_type = "WINDOW";
    bl_context = "data"
    #bl_category = "Tomte"

    def draw(self,context):

        layout = self.layout

        row = layout.row(align=True)
        row.alignment = 'EXPAND'

        row.operator("object.mybutton", text="Test").number=0.1
        #row.operator("object.my.button", text="10").number=0.1


class OBJECT_OT_MyOp(bpy.types.Operator): #The operator class derived from Operator
    bl_idname="object.mybutton" #Same as in row.operator
    bl_label="my.button blabla" #Needed

    number: bpy.props.FloatProperty() #The property used in row.operator

    def execute(self, context): #Is trigered by buttons
        print("Test", self.number) #With the associated value
        return {'FINISHED'}

def register():
    bpy.utils.register_class(PANEL1_PT_QuickWeightPanel)
    bpy.utils.register_class(OBJECT_OT_MyOp)


def unregister():
    bpy.utils.unregister_class(PANEL1_PT_QuickWeightPanel)
    bpy.utils.unregister_class(OBJECT_OT_MyOp)

if __name__ == "__main__":
    register()
