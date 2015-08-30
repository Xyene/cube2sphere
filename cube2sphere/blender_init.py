__author__ = 'Xyene'

import bpy
import sys
import math


bpy.context.scene.cycles.resolution_x = int(sys.argv[-5])
bpy.context.scene.cycles.resolution_y = int(sys.argv[-4])

for i, name in enumerate(['bottom', 'top', 'left', 'right', 'back', 'front']):
    bpy.data.images[name].filepath = "%s" % sys.argv[-6 - i]

camera = bpy.data.objects["Camera"]
camera.rotation_mode = 'XYZ'
camera.rotation_euler = (math.pi / 2 + float(sys.argv[-3]), float(sys.argv[-2]), float(sys.argv[-1]))

bpy.ops.render.render(animation=True)