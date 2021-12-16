with open("input3.txt") as file:
	report = file.read().splitlines()

def gamma_rate(num_list, bit_pos):
	ones = 0
	zeros = 0
	for number in num_list:
		if number[bit_pos] == '1':
			ones += 1
		else:
			zeros += 1
	if ones > zeros:
		return '1'
	elif zeros > ones:
		return '0'
	else:
		return '1'

def epsilon_rate(num_list, bit_pos):
	ones = 0
	zeros = 0
	for number in num_list:
		if number[bit_pos] == '1':
			ones += 1
		else:
			zeros += 1
	if ones < zeros:
		return '1'
	elif zeros < ones:
		return '0'
	else:
		return '0'

ogr = report.copy()
for bit in range(12):
	if len(ogr) > 1:
		gr = gamma_rate(ogr, bit)
		for value in reversed(ogr):
			if value[bit] != gr:
				ogr.remove(value)

csr = report.copy()
for bit in range(12):
	if len(csr) > 1:
		er = epsilon_rate(csr, bit)
		for value in reversed(csr):
			if value[bit] != er:
				csr.remove(value)

print("day3_2", int(ogr[0], 2) * int(csr[0], 2))  # 5941884
