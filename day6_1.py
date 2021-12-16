with open("input6.txt") as file:
    fish_list = file.readline().strip().split(',')

fishes = []
for fish in fish_list:
    fishes.append(int(fish))

for day in range(80):
    new_fish = []
    babies = 0
    for fish in fishes:
        if fish != 0:
            new_fish.append(fish - 1)
        else:
            new_fish.append(6)
            babies += 1
    for baby in range(babies):
        new_fish.append(8)
    fishes = new_fish.copy()

print("day6_1", len(fishes))  # 366057
