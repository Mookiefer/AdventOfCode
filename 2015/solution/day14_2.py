def solve():
	with open("input/input14.txt") as file:
		reindeer_raw = file.read().splitlines()

	reindeer_times = list()
	for index, item in enumerate(reindeer_raw):
		x1 = item.replace(" can fly", "")
		x2 = x1.replace(" km/s for", "")
		x3 = x2.replace(" seconds, but then must rest for", "")
		x4 = x3.replace(" seconds.", "")
		x5 = x4.split()
		reindeer = dict()
		reindeer["name"] = x5[0]
		reindeer["speed"] = int(x5[1])
		reindeer["endurance"] = int(x5[2])
		reindeer["rest"] = int(x5[3])
		reindeer["action"] = reindeer["endurance"]
		reindeer["resting"] = False
		reindeer["distance"] = 0
		reindeer["score"] = 0
		reindeer_times.append(reindeer)

	for time in range(2503):
		best_distance = 0
		for reindeer in reindeer_times:
			if reindeer["resting"]:
				reindeer["action"] -= 1
				if reindeer["action"] == 0:
					reindeer["resting"] = False
					reindeer["action"] = reindeer["endurance"]
			else:
				reindeer["distance"] += reindeer["speed"]
				reindeer["action"] -= 1
				if reindeer["action"] == 0:
					reindeer["resting"] = True
					reindeer["action"] = reindeer["rest"]
			if reindeer["distance"] > best_distance:
				best_distance = reindeer["distance"]
		for reindeer in reindeer_times:
			if reindeer["distance"] == best_distance:
				reindeer["score"] += 1

	best_score = 0
	for reindeer in reindeer_times:
		if reindeer["score"] > best_score:
			best_score = reindeer["score"]

	print("day14_2", best_score)  # 1256
