with open("input7.txt") as file:
	stuff = file.read().splitlines()

def chk(thing):
	key = thing[len(thing)-1]
	if key == 'a':
		key = 'zz'
	return str(len(key)) + key

parts = []
for index, item in enumerate(stuff):
	part = item.split(" ")
	parts.append(part)
sorted_stuff = sorted(parts, key=chk)

ans = {}

for item in sorted_stuff:
	if item[1] == '->':
		if item[0].isdigit():
			ans[item[2]] = int(item[0])
		else:
			ans[item[2]] = ans[item[0]]
	elif item[1] == 'AND':
		if item[0].isdigit():
			ans[item[4]] = int(item[0]) & ans[item[2]]
		else:
			ans[item[4]] = ans[item[0]] & ans[item[2]]
	elif item[1] == 'OR':
		ans[item[4]] = ans[item[0]] | ans[item[2]]
	elif item[1] == 'LSHIFT':
		ans[item[4]] = ans[item[0]] << int(item[2])
	elif item[1] == 'RSHIFT':
		ans[item[4]] = ans[item[0]] >> int(item[2])
	elif item[0] == 'NOT':
		ans[item[3]] = ~ ans[item[1]] & 65535

print("day7_1", ans['a'])  # 3176
