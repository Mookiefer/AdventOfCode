def solve():
	with open("input/input6.txt") as file:
		fish_list = file.read().split(',')

	ocean = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	for fish in fish_list:
		index = int(fish)
		ocean[index] += 1

	for day in range(256):
		new_ocean = [0, 0, 0, 0, 0, 0, 0, 0, 0]
		for index in range(8):
			new_ocean[index] = ocean[index + 1]
		new_ocean[8] = ocean[0]
		new_ocean[6] += ocean[0]
		ocean = new_ocean.copy()

	print("day6_2", sum(ocean))  # 1653559299811
