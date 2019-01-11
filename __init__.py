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
import math
from bpy import context, data, ops
from mathutils import Euler, Matrix, Quaternion, Vector

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def basic_closed_curve(name, p0, p1, p2, p3):
    # Create curve and cache reference.
    ops.curve.primitive_bezier_circle_add(enter_editmode=False)
    curve = context.active_object
    curve.name = 'Basic Closed Curve' + name
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

def basic_simple_curve(name, p0, p1):
    ops.curve.primitive_bezier_curve_add(enter_editmode=False)
    curve = context.active_object
    curve.name = 'Basic Simple Curve' + name
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

def single_hair(closed, simple, p0, p1, p3):
    ops.curve.primitive_bezier_curve_add(enter_editmode=False)
    curve = context.active_object
    curve.name = 'First Type'
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
    
    # Shape
    curve.data.bevel_object = bpy.data.objects[closed]
    curve.data.taper_object = bpy.data.objects[simple]
    
    # Transform
    bpy.context.scene.objects.active.scale = p3[0]
    bpy.context.scene.objects.active.rotation_euler = p3[1]
    bpy.context.scene.objects.active.location = p3[2]
    
# Front
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

first_closed = basic_closed_curve('01', p0, p1, p2, p3)

p4 = []
p4.append(Vector((1.6000, -0.3400, 0.0000)))
p4.append(Vector((-1.0000, 0.0000, 0.0000)))
p4.append(Vector((-0.5000, 0.2800, 0.0000)))

p5 = []
p5.append(Vector((0.3500, 0.3500, 0.0000)))
p5.append(Vector((1.0000, 0.0000, 0.0000)))
p5.append(Vector((1.9900, -0.1700, 0.0000)))

first_simple = basic_simple_curve('01', p4, p5)

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

second_closed = basic_closed_curve('02', p6, p7, p8, p9)

p10 = []
p10.append(Vector((1.6000, -0.3400, 0.0000)))
p10.append(Vector((-1.0000, 0.0000, 0.0000)))
p10.append(Vector((-0.5000, 0.2800, 0.0000)))

p11 = []
p11.append(Vector((0.5389, 1.4427, 0.0000)))
p11.append(Vector((1.0000, 0.0000, 0.0000)))
p11.append(Vector((1.9900, -0.1700, 0.0000)))

second_simple = basic_simple_curve('02', p10, p11)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

p12 = []
p12.append(Vector((0.1245, 0.2037, 0.0916)))
p12.append(Vector((0.0124, 0.1637, -0.0280)))
p12.append(Vector((0.2630, -0.8983, 0.3541)))

p13 = []
p13.append(Vector((0.1858, -2.2267, -0.9604)))
p13.append(Vector((1.0884, -2.2705, -3.0047)))
p13.append(Vector((0.4267, -1.6870, -1.9636)))

p14 = []
p14.append(Vector((0.7346, -0.3922, -0.3078)))
p14.append(Vector((math.radians(27.5962), math.radians(142.589), math.radians(-224.597))))
p14.append(Vector((-0.0715, -1.0689, 2.4231)))

single_hair(first_closed, first_simple, p12, p13, p14)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

p16 = []
p16.append(Vector((0.0474, 0.0234, -0.0433)))
p16.append(Vector((0.0211, 0.0141, -0.0278)))
p16.append(Vector((-0.4961, -1.8625, 0.3345)))

p17 = []
p17.append(Vector((0.6021, -2.3578, -1.2558)))
p17.append(Vector((-0.1304, -3.3095, -2.2563)))
p17.append(Vector((-0.3387, -0.2077, -0.1034)))

p18 = []
p18.append(Vector((-0.5161, -0.3922, -0.3078)))
p18.append(Vector((math.radians(43.0794), math.radians(175.762), math.radians(-204.492))))
p18.append(Vector((-0.0382, -1.0437, 2.4477)))


single_hair(first_closed, first_simple, p16, p17, p18)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

p19 = []
p19.append(Vector((0.0605, 0.0819, -0.0501)))
p19.append(Vector((0.0378, 0.0843, -0.0516)))
p19.append(Vector((-0.1054, -0.1891, 0.2761)))

p20 = []
p20.append(Vector((0.1418, -2.4546, 0.2383)))
p20.append(Vector((0.4127, -3.3218, -1.6458)))
p20.append(Vector((0.0087, 0.0489, 0.0797)))

p21 = []
p21.append(Vector((0.3078, 0.3078, 0.3078)))
p21.append(Vector((math.radians(-135.427), math.radians(181.645), math.radians(-173.21))))
p21.append(Vector((-0.0269, -1.0361, 2.4331)))

single_hair(first_closed, first_simple, p19, p20, p21)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

p22 = []
p22.append(Vector((0.0474, 0.0234, -0.0433)))
p22.append(Vector((0.0211, 0.0141, -0.0278)))
p22.append(Vector((0.1448, -0.4429, 0.4276)))

p23 = []
p23.append(Vector((-0.2247, -2.3724, 0.0233)))
p23.append(Vector((0.6031, -2.8554, -2.2048)))
p23.append(Vector((0.1264, 0.4731, -0.5563)))

p24 = []
p24.append(Vector((0.5161, 0.3922, 0.3078)))
p24.append(Vector((math.radians(-136.921), math.radians(184.238), math.radians(-155.508))))
p24.append(Vector((-0.0223, -1.0437, 2.4477)))

single_hair(first_closed, first_simple, p22, p23, p24)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

p25 = []
p25.append(Vector((0.2900, -0.0027, -0.2220)))
p25.append(Vector((0.1142, 0.0905, -0.1349)))
p25.append(Vector((0.3759, -0.3174, 0.6216)))

p26 = []
p26.append(Vector((-3.9942, -2.1316, -0.3099)))
p26.append(Vector((0.6691, -4.0723, -2.7557)))
p26.append(Vector((-3.7605, -0.7307, -0.2524)))

p27 = []
p27.append(Vector((0.1846, 0.3067, 0.3074)))
p27.append(Vector((math.radians(-148.388), math.radians(180.073), math.radians(-103.587))))
p27.append(Vector((-0.0174, -1.0428, 2.4287)))

single_hair(first_closed, first_simple, p25, p26, p27)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

p28 = []
p28.append(Vector((0.1997, 0.1810, 0.1567)))
p28.append(Vector((0.0876, 0.1410, 0.0372)))
p28.append(Vector((-0.0521, -1.2464, 0.2709)))

p29 = []
p29.append(Vector((0.6762, -1.8978, -0.4249)))
p29.append(Vector((0.6527, -2.6536, -3.4344)))
p29.append(Vector((-0.0091, -2.0702, -2.3932)))

p30 = []
p30.append(Vector((-0.7346, 0.3922, 0.3078)))
p30.append(Vector((math.radians(27.5962), math.radians(-37.4106), math.radians(-315.403))))
p30.append(Vector((0.0628, -1.0177, 2.4495)))


single_hair(first_closed, first_simple, p28, p29, p30)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

p31 = []
p31.append(Vector((0.1578, -1.2012, 0.4306)))
p31.append(Vector((0.2201, 0.4303, -0.4083)))
p31.append(Vector((-0.4468, -1.0094, 1.4471)))

p32 = []
p32.append(Vector((1.0629, -3.4865, -1.7192)))
p32.append(Vector((-0.0290, -3.8182, -3.8705)))
p32.append(Vector((0.6691, -2.8950, -1.7503)))

p33 = []
p33.append(Vector((-0.5161, 0.3922, 0.3078)))
p33.append(Vector((math.radians(48.489), math.radians(-21.9885), math.radians(-311.352))))
p33.append(Vector((0.2155, -1.0767, 2.4368)))


single_hair(first_closed, first_simple, p31, p32, p33)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

p34 = []
p34.append(Vector((-0.0413, -0.5441, -0.0555)))
p34.append(Vector((0.2038, 0.3199, -0.3361)))
p34.append(Vector((-0.4124, -1.1984, 0.8252)))

p35 = []
p35.append(Vector((-0.1608, -2.5737, -2.0292)))
p35.append(Vector((0.9169, -3.7260, -2.9079)))
p35.append(Vector((0.2441, -1.7120, 0.3762)))

p36 = []
p36.append(Vector((0.5161, -0.3922, -0.3078)))
p36.append(Vector((math.radians(48.489), math.radians(158.011), math.radians(-217.571))))
p36.append(Vector((-0.2381, -1.1318, 2.4473)))

single_hair(first_closed, first_simple, p34, p35, p36)
