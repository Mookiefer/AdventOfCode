def solve():
	with open("input/input9.txt") as file:
		travel_times_lists = file.read().splitlines()

	from itertools import permutations

	locations = set()
	travel_times = []
	for travel_times_list in travel_times_lists:
		x = travel_times_list.split(' ')
		locations.add(x[0])
		locations.add(x[2])
		travel_times.append([x[0], x[2], x[4]])

	worst_time = 0
	worst_path = list()
	for path in permutations(locations, len(locations)):
		this_time = 0
		for item in travel_times:
			for i in range(7):
				if path[i] in item and path[i+1] in item:
					this_time += int(item[2])
		if this_time > worst_time:
			worst_time = this_time
			worst_path = path

	print("day9_2", worst_time)  # 804
