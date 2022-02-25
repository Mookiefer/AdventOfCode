def solve():
	with open("input/input16.txt") as file:
		aunts_raw = file.read().splitlines()

	aunts = list()

	for item in aunts_raw:
		aunt = dict()
		new = item.replace('Sue ', '')
		new = new[:new.index(':')]
		aunt['Sue'] = new
		triple = item[item.index(':')+2:]
		for single in triple.split(', '):
			key, value = single.split(': ')
			aunt[key] = value
		aunts.append(aunt)

	aunt_sue = {
		"Sue": 0,
		"children": 3,
		"cats": 7,
		"samoyeds": 2,
		"pomeranians": 3,
		"akitas": 0,
		"vizslas": 0,
		"goldfish": 5,
		"trees": 3,
		"cars": 2,
		"perfumes": 1,
		}

	result = 0
	for aunt in aunts:
		i = 0
		for compound, value in aunt.items():
			if compound in ('cats', 'trees'):
				if aunt_sue[compound] < int(value):
					i += 1
			elif compound in ('pomeranians', 'goldfish'):
				if aunt_sue[compound] > int(value):
					i += 1
			else:
				if aunt_sue[compound] == int(value):
					i += 1
			if i == 3:
				result = aunt['Sue']

	print("day16_2", result)  # 405
