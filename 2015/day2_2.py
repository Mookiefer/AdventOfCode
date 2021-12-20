with open("input2.txt") as file:
	measurements = file.read().splitlines()

total_ribbon = 0
for measurement in measurements:
	l, w, h = measurement.split("x")
	bow = int(l) * int(w) * int(h)
	x = int(l) + int(w)
	y = int(w) + int(h)
	z = int(h) + int(l)
	if x <= y and x <= z:
		ribbon = 2 * x
	elif y <= x and y <= z:
		ribbon = 2 * y
	elif z <= x and z <= y:
		ribbon = 2 * z
	else:
		ribbon = 0
		print("What?")
	total_ribbon += ribbon + bow

print("day2_2", total_ribbon)  # 3812909
