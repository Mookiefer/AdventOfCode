def solve():
	with open("input/input15.txt") as file:
		ingredients_raw = file.read().splitlines()

	ingredients = list()
	for item in ingredients_raw:
		x1 = item.replace(":", ",").replace(", ", ",").replace(" ", ",")
		x2 = x1.split(",")
		ingredient = dict()
		ingredient["name"] = x2[0]
		for i in range(1, 10, 2):
			ingredient[x2[i]] = int(x2[i+1])
		ingredients.append(ingredient)

	high_score = 0
	for a in range(0, 101):
		for b in range(0, 101):
			for c in range(0, 101):
				for d in range(0, 101):
					if a + b + c + d == 100:
						ingredients[0]['quantity'] = a
						ingredients[1]['quantity'] = b
						ingredients[2]['quantity'] = c
						ingredients[3]['quantity'] = d

						capacity = 0
						durability = 0
						flavor = 0
						texture = 0
						for ingredient in ingredients:
							capacity += ingredient['quantity'] * ingredient['capacity']
							durability += ingredient['quantity'] * ingredient['durability']
							flavor += ingredient['quantity'] * ingredient['flavor']
							texture += ingredient['quantity'] * ingredient['texture']
						if capacity < 0:
							capacity = 0
						if durability < 0:
							durability = 0
						if flavor < 0:
							flavor = 0
						if texture < 0:
							texture = 0
						score = capacity * durability * flavor * texture
						if score > high_score:
							high_score = score

	print("day15_1", high_score)  # 21367368
