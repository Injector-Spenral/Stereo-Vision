import math

distance = 200

def degsin(num):
	return math.sin(math.radians(num))

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

