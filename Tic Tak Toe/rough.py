board = [' ' for _ in range(9)]
for row in [board[i*3:(i+1)*3] for i in range(3)]:
    number_board = [[str(i)for i in range(j*3,(j+1)*3)] for j in range(3)]
    for row in number_board:
        print('|'+'|'.join(row)+'|')

