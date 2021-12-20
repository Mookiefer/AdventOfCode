import hashlib

with open("input4.txt") as file:
	secret_key = file.read().strip()

x = 0
test = True
while test:
	x += 1
	str2hash = secret_key + str(x)

	result = hashlib.md5(str2hash.encode())
	prefix = result.hexdigest()[0:6]
	if prefix == "000000":
		test = False

print("day4_2", x)  # 9962624
