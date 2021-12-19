with open("input2.txt") as file:
	measurements = file.read().splitlines()

total_area = 0
for measurement in measurements:
	l, w, h = measurement.split("x")
	x = int(l) * int(w)
	y = int(w) * int(h)
	z = int(h) * int(l)
	if x <= y and x <= z:
		extra = x
	elif y <= x and y <= z:
		extra = y
	elif z <= x and z <= y:
		extra = z
	else:
		extra = 0
		print("What?")
	area = 2 * (x + y + z)
	total_area += area + extra

print("day2_1", total_area)  # 1598415
