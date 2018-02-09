import math
"""
fov = 60
focal_length = 125#mm
pixel_screen_length = 640
pixels_from_edge = 120
"""
def sin(num):
	return math.sin(math.radians(num))

def tan(num):
	return math.tan(math.radians(num))

def atan(num):
	return math.atan(math.radians(num))

def acos(num):
	return math.acos(math.radians(num))

def angleFind(fov, focal_length, pixel_screen_length, pixels_from_edge):
	half_fov = fov / 2
	other_angle = 90 - half_fov
	sensor_length = 2 * sin(half_fov) * focal_length / sin(other_angle)
	distance_from_edge_of_screen = sensor_length / (pixel_screen_length / pixels_from_edge)  
	distance_from_centre = sensor_length / 2 - distance_from_edge_of_screen
	hypo = math.sqrt(distance_from_centre ** 2 + focal_length ** 2)
	#angle_from_centre = atan(distance_from_centre / focal_length) * 10000
	#angle_from_centre2 = acos((hypo ** 2 + focal_length ** 2 - distance_from_centre ** 2) /  (2 * hypo * focal_length))
	angle_from_centre = math.degrees(math.atan(distance_from_centre  / focal_length))
	return sensor_length, distance_from_edge_of_screen, distance_from_centre, angle_from_centre

