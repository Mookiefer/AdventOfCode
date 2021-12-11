x_pos = 0
z_pos = 0
aim = 0

with open("input2.txt") as file:
	instructions = file.read().splitlines()

for course in instructions:
	amount = int(course[-1:])
	if course[0:1] == 'f':
		x_pos += amount
		z_pos += aim * amount
	elif course[0:1] == 'd':
		aim += amount
	elif course[0:1] == 'u':
		aim -= amount
	else:
		print("What?!?")

print(x_pos * z_pos)
