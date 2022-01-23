def solve():
	with open("input/input3.txt") as file:
		directions = file.read()

	homes = {(0, 0)}
	santa = [0, 0]
	robot = [0, 0]
	is_real_santa = True
	for direction in directions:
		if is_real_santa:
			location = santa
		else:
			location = robot
		match direction:
			case "^":
				location[1] += 1
			case ">":
				location[0] += 1
			case "v":
				location[1] -= 1
			case "<":
				location[0] -= 1
			case _:
				print("What?")
		homes.add(tuple(location))
		is_real_santa = not is_real_santa

	print("day3_2", len(homes))  # 2639
