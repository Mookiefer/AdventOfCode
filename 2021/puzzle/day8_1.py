def solve():
	with open("input/input8.txt") as file:
		display = file.read().splitlines()

	digits = []
	output = []
	for item in display:
		temp = item.split(" | ")
		temp0 = temp[0]
		digits.append(temp0.split())
		temp1 = temp[1]
		output.append(temp1.split())

	count = 0
	for element in output:
		for code in element:
			if len(code) in (2, 3, 4, 7):
				count += 1

	print("day8_1", count)  # 473
