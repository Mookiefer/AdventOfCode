with open("input3.txt") as file:
	directions = file.read().strip()

homes = {(0, 0)}
location = [0, 0]
for direction in directions:
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

print("day3_1", len(homes))  # 2565
