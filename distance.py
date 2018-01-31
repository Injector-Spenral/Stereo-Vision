"""
This module calculates how far away an object is based on the angles it is in relation to 2 cameras,
as well as the distance between the cameras. It also has another function(still in early testing) which
could use multiple cameras to find the distanced more accurately
"""

import math

def degsin(num): #This function makes it easier to use degrees with the math.sin() function, which normally uses radians
	return math.sin(math.radians(num))

focal_length = 304
horizontal_fov = 62.2
vertical_fov = 48.8
frame_width = 640
frame_height = 480
half = horizontal_fov / 2
c = 180 - 90 - half
distance = 200
focal_width = degsin(half) * focal_length / degsin(c) * 2

def calculate(angle1, angle2, distance = 20):
	side1 = distance
	angle3 = 180 - angle1 - angle2
	side2 = (degsin(angle2) * side1) / degsin(angle3)
	side3 = (degsin(angle1) * side2)
	side4 = math.sqrt(side2**2-side3**2)
	return side3, side4

def calc3Angles(angle4, angle5, angle6, distance1 = 20, distance2 = 10):
	x = calcDatBoi(angle4, angle5, distance2)[0]
	y = calcDatBoi(angle4, angle6, distance1)[0]
	z = calcDatBoi(180-angle5, angle6, distance1-distance2)[0]
	a = (x + y + y + z) / 4
	return x, y, z, a

