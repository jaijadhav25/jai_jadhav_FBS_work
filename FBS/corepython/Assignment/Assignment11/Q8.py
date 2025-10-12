# 8. Print 1 to 100 in snakes and ladder pattern.

def snake_board():
    board = []
    for i in range(9, -1, -1):
        row = []
        for j in range(i * 10 + 1, i * 10 + 11):
            row.append(j)
        if(i % 2 != 0):
            row.reverse()
            board.append(row)
        else:
            board.append(row)
    print(board)


snake_board()
