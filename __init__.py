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

def basic_closed_curve():
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
    bez_points[0].co = Vector((0, -0.45, 0.0))
    bez_points[0].handle_left = Vector((-0.55, -0.45, 0.0)
    bez_points[0].handle_right = Vector((0.55, -0.45, 0.0))

    # Top-middle point.
    bez_points[1].co = Vector((1.0, 0.0, 0.0))
    bez_points[1].handle_left = Vector((1.0, -0.18, 0.0))
    bez_points[1].handle_right = Vector((1.0, 0.18, 0.0))

    # Right point.
    bez_points[2].co = Vector((0, 0.45, 0.0))
    bez_points[2].handle_left = Vector((0.55, 0.45, 0.0))
    bez_points[2].handle_right = Vector((-0.55, 0.45, 0.0))

    # Bottom point.
    bez_points[3].co = Vector((-1.0, 0.0, 0.0))
    bez_points[3].handle_left = Vector((-1.0, 0.18, 0.0))
    bez_points[3].handle_right = Vector((-1.0, -0.18, 0.0))
    
    return curve.name

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def basic_simple_curve():
    ops.curve.primitive_bezier_curve_add(enter_editmode=False)
    curve = context.active_object
    curve.name = 'Basic Simple Curve'
    bez_points = curve.data.splines[0].bezier_points

    # Set handles to desired handle type.
    for bez_point in bez_points:
        bez_point.handle_left_type = 'FREE'
        bez_point.handle_right_type = 'FREE'   

    # First point.
    bez_points[0].co = Vector((-1.0, 0.0, 0.0))
    bez_points[0].handle_left = Vector((1.6, -0.34, 0.0))
    bez_points[0].handle_right = Vector((-0.5, 0.28, 0.0))

    # Second point.
    bez_points[1].co = Vector((1.0, 0.0, 0.0))
    bez_points[1].handle_left = Vector((0.35, 0.35, 0.0))
    bez_points[1].handle_right = Vector((1.99, -0.17, 0.0))
    
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
    bez_points[0].handle_left = Vector((0.0, 0.0, 0.0))
    bez_points[0].handle_right = Vector((0.0, -0.5, 0.0))

    # Second point.
    bez_points[1].co = Vector((0.0, -2.0, 0.0))
    bez_points[1].handle_left = Vector((0.0, -1.0, 0.0))
    bez_points[1].handle_right = Vector((0.0, -0.0, 0.0))
    
    # Shape
    curve.data.bevel_object = bpy.data.objects[closed]
    curve.data.taper_object = bpy.data.objects[simple]

first_closed = basic_closed_curve()
first_simple = basic_simple_curve()
single_hair(first_closed, first_simple)
