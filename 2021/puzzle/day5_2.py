def solve():
	with open("input/input5.txt") as file:
		lines = file.read().splitlines()

	for index, line in enumerate(lines):
		lines[index] = line.split(' -> ')

	for i, line in enumerate(lines):
		for j, coord in enumerate(line):
			lines[i][j] = coord.split(',')

	matrix = []
	for x in range(1000):
		hold = []
		for y in range(1000):
			hold.append(0)
		matrix.append(hold)

	for line in lines:
		x1 = int(line[0][0])
		x2 = int(line[1][0])
		y1 = int(line[0][1])
		y2 = int(line[1][1])
		if x1 == x2:
			if y1 > y2:
				y1, y2 = y2, y1
			for i in range(y2 - y1 + 1):
				matrix[x1][y1 + i] += 1
		elif y1 == y2:
			if x1 > x2:
				x1, x2 = x2, x1
			for i in range(x2 - x1 + 1):
				matrix[x1 + i][y1] += 1
		else:
			if x1 > x2:
				x1, x2 = x2, x1
				y1, y2 = y2, y1
			for i in range(x2 - x1 + 1):
				if y1 > y2:
					matrix[x1 + i][y1 - i] += 1
				else:
					matrix[x1 + i][y1 + i] += 1

	count = 0
	for i, x in enumerate(matrix):
		for j, y in enumerate(x):
			if y > 1:
				count += 1

	print("day5_2", count)  # 19939
