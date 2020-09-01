bl_info = {
    "name": "Quick Smooth",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import math

class ObjectQuickSmooth(bpy.types.Operator):
    """Quick Smooth"""
    bl_idname = "object.quicksmooth"
    bl_label = "Quick Smooth object"

    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'

    def execute(self, context):
        if bpy.context.object.data.use_auto_smooth:
            bpy.ops.object.shade_flat()
            bpy.context.object.data.use_auto_smooth = False
        else:
            bpy.ops.object.shade_smooth()
            bpy.context.object.data.use_auto_smooth = True
            bpy.context.object.data.auto_smooth_angle = math.radians(30)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(ObjectQuickSmooth)


def unregister():
    bpy.utils.unregister_class(ObjectQuickSmooth)


if __name__ == "__main__":
    register()
