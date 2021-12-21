with open("input9.txt") as file:
	puzzle_input = file.read().splitlines()

height_map = []
for index, line in enumerate(puzzle_input):
	height_map.append([])
	for number in line:
		height_map[index].append(int(number))

def check_height(x, y, hmap):
	test = hmap[x][y]
	if (x != 0) and (test >= hmap[x-1][y]):
		return 0
	elif (y != 0) and (test >= hmap[x][y-1]):
		return 0
	elif (x != 99) and (test >= hmap[x+1][y]):
		return 0
	elif (y != 99) and (test >= hmap[x][y+1]):
		return 0
	else:
		return test + 1

level = 0
for i in range(100):
	for j in range(100):
		level += check_height(i, j, height_map)

print("day9_1", level)  # 423
