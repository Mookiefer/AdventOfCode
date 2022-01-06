with open("input14.txt") as file:
	reindeer_raw = file.read().splitlines()

reindeer_times = list()
for item in reindeer_raw:
	x1 = item.replace("can fly ", "")
	x2 = x1.replace("km/s for ", "")
	x3 = x2.replace("seconds, but then must rest for ", "")
	x4 = x3.replace(" seconds.", "")
	reindeer_times.append(x4.split())

best_distance = 0
for reindeer in reindeer_times:
	name = reindeer[0]
	speed = int(reindeer[1])
	endurance = int(reindeer[2])
	rest = int(reindeer[3])
	distance = 0
	resting = False
	action = endurance
	for time in range(2503):
		if resting:
			action -= 1
			if action == 0:
				resting = False
				action = endurance
		else:
			distance += speed
			action -= 1
			if action == 0:
				resting = True
				action = rest
	if distance > best_distance:
		best_distance = distance

print("day14_1", best_distance)  # 2660
