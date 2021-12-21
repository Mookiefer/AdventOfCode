with open("input8.txt") as file:
	display = file.read().splitlines()

digits = []
output = []
for item in display:
	temp = item.split(" | ")
	temp0 = temp[0]
	digits.append(temp0.split())
	temp1 = temp[1]
	output.append(temp1.split())

def find_nums(clues):
	nums = {}
	test = ''
	codes = sorted(clues, key=len)
	for code in codes:
		match len(code):
			case 2:
				nums[1] = code
			case 3:
				nums[7] = code
			case 4:
				nums[4] = code
				test = set(nums[4]) - set(nums[7])
			case 5:
				if all(elem in code for elem in nums[1]):
					nums[3] = code
				elif all(elem in code for elem in test):
					nums[5] = code
				else:
					nums[2] = code
			case 6:
				if not all(elem in code for elem in nums[1]):
					nums[6] = code
				elif all(elem in code for elem in nums[4]):
					nums[9] = code
				else:
					nums[0] = code
			case 7:
				nums[8] = code
	return nums

def crack_output(numbers, cypher):
	total = ''
	for letter in cypher:
		for key, value in numbers.items():
			if sorted(letter) == sorted(value):
				total += str(key)
	return int(total)

code_sum = 0
for index, element in enumerate(digits):
	x = find_nums(element)
	code_sum += crack_output(x, output[index])

print("day8_2", code_sum)  # 1097568
