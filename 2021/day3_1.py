gamma_rate = ''
epsilon_rate = ''
ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open("input3.txt") as file:
	report = file.read().splitlines()

for number in report:
	for bit in range(12):
		if number[bit] == '1':
			ones[bit] += 1

for count in ones:
	if count > 500:
		gamma_rate += '1'
		epsilon_rate += '0'
	else:
		gamma_rate += '0'
		epsilon_rate += '1'
		
gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print("day3_1", gamma_rate * epsilon_rate)  # 4006064
