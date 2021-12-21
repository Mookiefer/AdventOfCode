with open("input2.txt") as file:
	instructions = file.read().splitlines()

x_pos = 0
z_pos = 0

for course in instructions:
	amount = int(course[-1:])
	if course[0:1] == 'f':
		x_pos += amount
	elif course[0:1] == 'd':
		z_pos += amount
	elif course[0:1] == 'u':
		z_pos -= amount
	else:
		print("What?!?")

print("day2_1", x_pos * z_pos)  # 1580000
