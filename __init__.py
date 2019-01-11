# Anime Hair Generator
# Copyright © 2019 Mateusz Dera

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import bpy
from bpy import context, data, ops
from mathutils import Euler, Matrix, Quaternion, Vector

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def basic_closed_curve(p0, p1, p2, p3):
    # Create curve and cache reference.
    ops.curve.primitive_bezier_circle_add(enter_editmode=False)
    curve = context.active_object
    curve.name = 'Basic Closed Curve'
    bez_points = curve.data.splines[0].bezier_points

    # Set handles to desired handle type.
    for bez_point in bez_points:
        bez_point.handle_left_type = 'FREE'
        bez_point.handle_right_type = 'FREE'   

    # Left point.
    bez_points[0].co = p0[1]
    bez_points[0].handle_left = p0[0]
    bez_points[0].handle_right = p0[2]

    # Top-middle point.
    bez_points[1].co = p1[1]
    bez_points[1].handle_left = p1[0]
    bez_points[1].handle_right = p1[2]

    # Right point.
    bez_points[2].co = p2[1]
    bez_points[2].handle_left = p2[0]
    bez_points[2].handle_right = p2[2]

    # Bottom point.
    bez_points[3].co = p3[1]
    bez_points[3].handle_left = p3[0]
    bez_points[3].handle_right = p3[2]
    
    return curve.name

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def basic_simple_curve(p0, p1):
    ops.curve.primitive_bezier_curve_add(enter_editmode=False)
    curve = context.active_object
    curve.name = 'Basic Simple Curve'
    bez_points = curve.data.splines[0].bezier_points

    # Set handles to desired handle type.
    for bez_point in bez_points:
        bez_point.handle_left_type = 'FREE'
        bez_point.handle_right_type = 'FREE'   

    # First point.
    bez_points[0].co = p0[1]
    bez_points[0].handle_left = p0[0]
    bez_points[0].handle_right = p0[2]

    # Second point.
    bez_points[1].co = p1[1]
    bez_points[1].handle_left = p1[0]
    bez_points[1].handle_right = p1[2]
    
    return curve.name

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def single_hair(closed, simple):
    ops.curve.primitive_bezier_curve_add(enter_editmode=False)
    curve = context.active_object
    curve.name = 'First Type'
    bez_points = curve.data.splines[0].bezier_points

    # Set handles to desired handle type.
    for bez_point in bez_points:
        bez_point.handle_left_type = 'FREE'
        bez_point.handle_right_type = 'FREE'   

    # First point.
    bez_points[0].co = Vector((0.0, 0.0, 0.0))
    bez_points[0].handle_left = Vector((0.0, 0.5, 0.0))
    bez_points[0].handle_right = Vector((0.0, -0.5, 0.0))

    # Second point.
    bez_points[1].co = Vector((0.0, -2.0, 0.0))
    bez_points[1].handle_left = Vector((0.0, -1.0, 0.0))
    bez_points[1].handle_right = Vector((0.0, -3.0, 0.0))
    
    # Shape
    curve.data.bevel_object = bpy.data.objects[closed]
    curve.data.taper_object = bpy.data.objects[simple]

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

p0 = []
p0.append(Vector((-0.5500, -0.4500, 0.0000)))
p0.append(Vector((0.0000, -0.4500, 0.0000)))
p0.append(Vector((0.5500, -0.4500, 0.0000)))

p1 = []
p1.append(Vector((1.0000, -0.1800, 0.0000)))
p1.append(Vector((1.0000, 0.0000, 0.0000)))
p1.append(Vector((0.8198, 0.2332, 0.0000)))

p2 = []
p2.append(Vector((0.6908, 0.6175, 0.0000)))
p2.append(Vector((-0.0639, 0.5629, 0.0000)))
p2.append(Vector((-0.2992, 0.5264, 0.0000)))

p3 = []
p3.append(Vector((-0.9409, 0.2253, 0.0000)))
p3.append(Vector((-1.0000, 0.0000, 0.0000)))
p3.append(Vector((-1.0000, -0.1800, 0.000)))

first_closed = basic_closed_curve(p0, p1, p2, p3)

p4 = []
p4.append(Vector((1.6000, -0.3400, 0.0000)))
p4.append(Vector((-1.0000, 0.0000, 0.0000)))
p4.append(Vector((-0.5000, 0.2800, 0.0000)))

p5 = []
p5.append(Vector((0.3500, 0.3500, 0.0000)))
p5.append(Vector((1.0000, 0.0000, 0.0000)))
p5.append(Vector((1.9900, -0.1700, 0.0000)))

first_simple = basic_simple_curve(p4, p5)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

p6 = []
p6.append(Vector((-0.5500, 0.0082, -0.0174)))
p6.append(Vector((0.0000, 0.0082, -0.0174)))
p6.append(Vector((0.5500, 0.0082, -0.0174)))

p7 = []
p7.append(Vector((1.0000, -0.1800, -0.0174)))
p7.append(Vector((1.0000, 0.0000, -0.0174)))
p7.append(Vector((0.8455, 0.3240, -0.0174)))

p8 = []
p8.append(Vector((0.0944, 0.5268, -0.0174)))
p8.append(Vector((-0.0902, 0.4995, -0.0174)))
p8.append(Vector((-0.3255, 0.4631, -0.0174)))

p9 = []
p9.append(Vector((-0.8818, 0.0084, -0.0174)))
p9.append(Vector((-1.0000, -0.2153, -0.0174)))
p9.append(Vector((-1.0000, -0.3953, -0.0174)))

second_closed = basic_closed_curve(p6, p7, p8, p9)

single_hair(first_closed, first_simple)