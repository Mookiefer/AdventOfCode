import json

with open("input12.txt") as file:
	stuff = json.load(file)

def flatten(obj):
	if type(obj) is str:
		return 0
	if type(obj) is int:
		return obj
	if type(obj) is dict:
		val = obj.values()
		if "red" in val:
			return 0
		return sum(map(flatten, val))
	if type(obj) is list:
		return sum(map(flatten, obj))

numbers = flatten(stuff)

print("day12_2", numbers)  # 96852
