with open("input4.txt") as file:
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

for draw in draws:
    winners = []
    score = 0
    for index, board in enumerate(boards):
        for x in range(5):
            for y in range(5):
                if board[x][y] == draw:
                    board[x][y] = 'X'
                    if check_win(board):
                        winners.append(index)
                        score = score_win(board)
    for win in reversed(winners):
        del boards[win]
    if len(boards) == 0:
        print("day4_2", int(draw) * score)  # 4880
        break
