def solve():
	with open("input/input4.txt") as file:
		draws = file.readline().strip().split(',')
		board_lines = file.read().strip().splitlines()

	boards = [[]]
	count = 0
	for line in board_lines:
		if line != '':
			boards[count].append(line.strip().split())
		else:
			boards.append([])
			count += 1

	def check_win(bingo):
		for i in range(5):
			if bingo[i][i] == 'X':
				row = True
				for j in range(5):
					if bingo[i][j] != 'X':
						row = False
						break
				column = True
				for j in range(5):
					if bingo[j][i] != 'X':
						column = False
						break
				if row or column:
					return True
		return False

	def score_win(bingo):
		board_score = 0
		for i in range(5):
			for j in range(5):
				if bingo[i][j] != 'X':
					board_score += int(bingo[i][j])
		return board_score

	winner = False
	score = 0
	value = 0
	for draw in draws:
		for board in boards:
			for x in range(5):
				for y in range(5):
					if board[x][y] == draw:
						board[x][y] = 'X'
						winner = check_win(board)
						score = score_win(board)
						value = int(draw)
		if winner:
			print("day4_1", score * value)  # 16716
			break
