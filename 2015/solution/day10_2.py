def solve():
	with open("input/input10.txt") as file:
		seed_key = file.read()

	count = 1
	for x in range(50):
		answer = ''
		for i in range(len(seed_key)):
			if count > 1:
				count -= 1
				continue
			num = seed_key[i]
			for j in range(i+1, len(seed_key)):
				if seed_key[j] == num:
					count += 1
				else:
					answer += str(count) + num
					break
		seed_key = answer + '\n'

	print("day10_2", len(seed_key.strip()))  # 6989950
