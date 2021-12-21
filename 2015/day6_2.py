with open("input6.txt") as file:
	instructions = file.read().strip().splitlines()

lights = [[0 for row in range(1000)] for column in range(1000)]

def switch_lights(table, codes, mode):
	# pass
	pointa = codes[0].split(",")
	pointb = codes[1].split(",")
	for x in range(int(pointa[0]), int(pointb[0])+1):
		for y in range(int(pointa[1]), int(pointb[1])+1):
			match mode:
				case "on":
					table[x][y] += 1
				case "off":
					if table[x][y] != 0:
						table[x][y] -= 1
				case "tog":
					table[x][y] += 2

for instruction in instructions:
	if "turn on" in instruction:
		corners = instruction[8:].split(" through ")
		action = "on"
	elif "turn off" in instruction:
		corners = instruction[9:].split(" through ")
		action = "off"
	elif "toggle" in instruction:
		corners = instruction[7:].split(" through ")
		action = "tog"
	else:
		print("What?")
	switch_lights(lights, corners, action)

lit = 0
for light_row in lights:
	for light in light_row:
		lit += light

print("day6_2", lit)  # 15343601
