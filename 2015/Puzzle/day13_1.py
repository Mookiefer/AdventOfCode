def solve():
	from itertools import permutations

	with open("input/input13.txt") as file:
		seats_raw = file.read().splitlines()

	seats_1 = [seat.replace(" would ", " ") for seat in seats_raw]
	remove = " happiness units by sitting next to "
	seats_2 = [seat.replace(remove, " ") for seat in seats_1]
	seats_3 = [seat.replace(".", "") for seat in seats_2]
	seats = [seat.split() for seat in seats_3]

	people = set()
	pairs = dict()
	for seat in seats:
		people.add(seat[0])
		pair = seat[0] + "-" + seat[3]
		if seat[1] == "lose":
			pairs[pair] = int("-" + seat[2])
		elif seat[1] == "gain":
			pairs[pair] = int(seat[2])
		else:
			print("What?")

	people_perms = permutations(people)

	best_perm = 0
	for group in people_perms:
		this_perm = 0
		perm_group = list()
		for x in range(len(group)-1):
			perm_group.append(pairs[group[x] + "-" + group[x+1]])
			perm_group.append(pairs[group[x+1] + "-" + group[x]])
		perm_group.append(pairs[group[7] + "-" + group[0]])
		perm_group.append(pairs[group[0] + "-" + group[7]])
		this_perm += sum(perm_group)
		if this_perm > best_perm:
			best_perm = this_perm

	print("day13_1", best_perm)  # 618
