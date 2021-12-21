with open("input6.txt") as file:
	instructions = file.read().splitlines()

lights = [[False for row in range(1000)] for column in range(1000)]

def switch_lights(table, codes, mode):
	# pass
	pointa = codes[0].split(",")
	pointb = codes[1].split(",")
	for x in range(int(pointa[0]), int(pointb[0])+1):
		for y in range(int(pointa[1]), int(pointb[1])+1):
			match mode:
				case "on":
					table[x][y] = True
				case "off":
					table[x][y] = False
				case "tog":
					table[x][y] = not table[x][y]

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
		if light:
			lit += 1

print("day6_1", lit)  # 400410
