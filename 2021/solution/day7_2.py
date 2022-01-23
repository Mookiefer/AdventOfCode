def solve():
	with open("input/input7.txt") as file:
		position_list = file.read().split(',')

	crabs = []
	for position in position_list:
		crabs.append(int(position))

	best_fuel = 100000000
	for index in range(max(crabs)):
		fuel = 0
		for crab in crabs:
			n = abs(crab - index)
			fuel += int(n * (n + 1) / 2)
		if fuel < best_fuel:
			best_fuel = fuel

	print("day7_2", best_fuel)  # 93699985
