with open("input8.txt") as file:
	santa_list = file.read().splitlines()

real_count = 0
string_count = 0
for item in santa_list:
	real_count += len(item)
	sub = ''
	for index, char in enumerate(item):
		if char == '\\':
			sub += '00'
		elif char == '\"':
			sub += '00'
		else:
			sub += char
	string_count += len(sub) + 2
diff = string_count - real_count

print("day8_2", diff)  # 2074
