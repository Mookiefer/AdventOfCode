def solve():
	with open("input/input1.txt") as file:
		depths = file.read().splitlines()

	count = 0
	depth_1 = None
	depth_2 = None
	depth_3 = None

	for depth in depths:
		depth = int(depth)
		if depth_1 is None:
			depth_1 = depth
			continue
		elif depth_2 is None:
			depth_2 = depth
			continue
		elif depth_3 is None:
			depth_3 = depth
			last_triad = depth_1 + depth_2 + depth_3
		else:
			depth_1 = depth_2
			depth_2 = depth_3
			depth_3 = depth
		if (triad := depth_1 + depth_2 + depth_3) > last_triad:
			count += 1
		last_triad = triad

	print("day1_2", count)  # 1645
