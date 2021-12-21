with open("input1.txt") as file:
	directions = file.read()

floor = 0
for direction in directions:
	match direction:
		case "(":
			floor += 1
		case ")":
			floor -= 1
		case _:
			print("What?")

print("day1_1", floor)  # 280
