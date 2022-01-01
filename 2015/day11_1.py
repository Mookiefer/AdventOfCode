with open("input11.txt") as file:
	pwd = file.read().strip()

pwd_list = [letter for letter in pwd]

def letter_change(word, index):
	change = word
	if word[index] == 'z':
		change[index] = 'a'
		letter_change(word, index-1)
	else:
		new_letter = chr(ord(word[index]) + 1)
		if new_letter in ['i', 'o', 'l']:
			new_letter = chr(ord(word[index]) + 2)
		change[index] = new_letter
	return change

def find_pairs(word):
	found_pair = False
	pairs = 0
	for index in range(len(word)-1):
		if found_pair:
			found_pair = False
			continue
		if word[index] == word[index + 1]:
			pairs += 1
			found_pair = True
	return pairs

def find_seq(word):
	for index in range(len(word)-2):
		if ord(word[index]) == ord(word[index + 1]) - 1:
			if ord(word[index]) == ord(word[index + 2]) - 2:
				return True
	return False

found = 0
while found < 1:
	pwd_list = letter_change(pwd_list, len(pwd_list)-1)
	if find_pairs(pwd_list) >= 2:
		if find_seq(pwd_list):
			new_pwd = ''.join(pwd_list)
			found += 1

print("day11_1", new_pwd)  # cqjxxyzz
