def solve():
	with open("input/input5.txt") as file:
		santa_list = file.read().splitlines()

	nice = 0
	bad = ("ab", "cd", "pq", "xy")
	vowels = "aeiou"
	for child in santa_list:
		if any(sub in child for sub in bad):
			continue
		double = False
		count = 0
		for letter in child:
			if letter in vowels:
				count += 1
			if (letter + letter) in child:
				double = True
		if count < 3 or not double:
			continue
		nice += 1

	print("day5_1", nice)  # 238
