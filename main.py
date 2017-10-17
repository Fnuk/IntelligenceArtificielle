from Play import Player

board = []

for i in range(11):
    board.append([0] * 11)

if __name__ == '__main__':

    moi = Player()

    moi.move(board, -1)

    for i in range(11):
        print(board[i])