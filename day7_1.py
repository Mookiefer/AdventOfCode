with open("input7.txt") as file:
    position_list = file.readline().strip().split(',')

crabs = []
for position in position_list:
    crabs.append(int(position))

best_fuel = 1000000
for index in range(max(crabs)):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - index)
    if fuel < best_fuel:
        best_fuel = fuel

print("day7_1", best_fuel)  # 344605