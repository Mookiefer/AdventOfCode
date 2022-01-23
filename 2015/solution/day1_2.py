def solve():
	with open("input/input1.txt") as file:
		directions = file.read()

	floor = 0
	basement = 0
	for index, direction in enumerate(directions):
		match direction:
			case "(":
				floor += 1
			case ")":
				floor -= 1
				if floor == -1:
					basement = index + 1
					break
			case _:
				print("What?")

	print("day1_2", basement)  # 1797
