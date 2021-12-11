count = 0
last_depth = None

with open("input1.txt") as file:
	depths = file.readlines()
	
for depth in depths:
	depth = int(depth)
	if last_depth is None:
		last_depth = depth
		continue
	if depth > last_depth:
		count += 1
	last_depth = depth

print(count)
