with open("input8.txt") as file:
	santa_list = file.read().splitlines()

real_count = 0
string_count = 0
for item in santa_list:
	real_count += len(item)
	sub = ''
	x = 0
	for index, char in enumerate(item):
		if x > 0:
			x -= 1
			continue
		elif char == '\\':
			pair = char + item[index+1]
			if pair == r'\\':
				sub += '0'
				x = 1
			elif pair == r'\"':
				sub += '0'
				x = 1
			elif pair == r'\x':
				sub += '0'
				x = 3
		else:
			sub += char
	string_count += len(sub) - 2

diff = real_count - string_count

print("day8_1", diff)  # 1342
