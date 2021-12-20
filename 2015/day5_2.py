import re

with open("input5.txt") as file:
	santa_list = file.read().strip().splitlines()

nice = 0
for child in santa_list:
	pair = False
	repeat = False
	last_letter = " "
	hold1 = ""
	hold2 = ""
	for letter in child:
		if re.search(f"{letter}.{letter}", child):
			repeat = True
			hold1 = letter
		if len(re.findall(f"{last_letter}{letter}", child)) > 1:
			pair = True
			hold2 = last_letter + letter
		last_letter = letter
	if pair and repeat:
		nice += 1

print("day5_2", nice)  # 69
