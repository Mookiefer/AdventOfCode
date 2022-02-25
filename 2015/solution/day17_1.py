def solve():
	from itertools import combinations

	with open("input/input17.txt") as file:
		raw = file.read().splitlines()

	containers = list()
	for item in raw:
		containers.append(int(item))

	result = 0
	for size in range(len(containers)+1):
		for combo in combinations(containers, size):
			if sum(combo) == 150:
				result += 1

	print("day17_1", result)  # 654
