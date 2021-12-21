import hashlib

with open("input4.txt") as file:
	secret_key = file.read()

x = 0
test = True
while test:
	x += 1
	str2hash = secret_key + str(x)

	result = hashlib.md5(str2hash.encode())
	prefix = result.hexdigest()[0:5]
	if prefix == "00000":
		test = False

print("day4_1", x)  # 282749
