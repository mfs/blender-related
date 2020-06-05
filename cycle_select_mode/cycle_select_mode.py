# ##### BEGIN GPL LICENSE BLOCK #####
#
# Copyright (C) 2020  Mike Sampson <mfs@sda.io>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Cycle Select Mode",
    "blender": (2, 80, 0),
    "category": "Mesh",
}


import bpy
from bpy.props import EnumProperty

class MeshCycleSelectMode(bpy.types.Operator):
    """Mesh Cycle Select Mode"""
    bl_idname = "mesh.cycle_select_mode"
    bl_label = "Cycle Select Mode"

    direction = EnumProperty(items=[('NEXT', 'Next', 'next'), ('PREV', 'Prev', 'prev')])

    @classmethod
    def poll(cls, context):
        return context.mode == 'EDIT_MESH'

    def execute(self, context):

        CYCLE_NEXT = {
            (True, False, False): (False, True, False),
            (False, True, False): (False, False, True),
            (False, False, True): (True, False, False),
        }

        CYCLE_PREV = { v: k for k, v in CYCLE_NEXT.items()}

        CYCLE = {'NEXT': CYCLE_NEXT, 'PREV': CYCLE_PREV}

        context.tool_settings.mesh_select_mode = CYCLE[self.direction][tuple(context.tool_settings.mesh_select_mode)]

        return {'FINISHED'}


def register():
    bpy.utils.register_class(MeshCycleSelectMode)


def unregister():
    bpy.utils.unregister_class(MeshCycleSelectMode)


if __name__ == "__main__":
    register()
