from EvaluationFunction import EvaluationFunction
import random
import time


class Player(object):
    startTime = 0
    maxTime = 0.4

    def play(self, board, player):
        startTime = time.time()
        first_play = True

        for a in range(11):
            if (board[a].count(1) or board[a].count(-1)):
                first_play = False

        if (first_play):
            board[5][5] = player
        else:
            max = -10000
            i = 0
            j = 0
            maxi = 0
            maxj = 0
            tmp = 0

            for i in range(11):
                for j in range(11):
                    if board[i][j] == 0:
                        board[i][j] = player
                        tmp = self.Min(board, 4, player)
                        if tmp > max or ((tmp == max) and (random.randint(0, 1000) % 2 == 0)):
                            max = tmp;
                            maxi = i;
                            maxj = j;
                        board[i][j] = 0

            return (maxi, maxj)

    def Max(self, board, profondeur, joueur):
        actualTime = startTime - time.time()

        if profondeur == 0 or board.winner() == True or actualTime > maxTime:
            return EvaluationFunction()

        max = -10000
        i = 0
        j = 0
        tmp = 0

        for i in range(11):
            for j in range(11):
                if board[i][j] == 0:
                    board[i][j] = joueur
                    tmp = self.Min(board, profondeur - 1, joueur)
                    if (tmp > max or ((tmp == max) and (random.randint(0, 1000) % 2 == 0))):
                        max = tmp
                    board[i][j] = 0

        return max


    def Min(self, board, profondeur, joueur):
        actualTime = startTime - time.time()

        if profondeur == 0 or board.winner() == True or actualTime > maxTime:
            return EvaluationFunction()

        min = 10000
        i = 0
        j = 0
        tmp = 0

        for i in range(11):
            for j in range(11):
                if board[i][j] == 0:
                    board[i][j] = joueur
                    tmp = self.Max(board, profondeur - 1, joueur)
                    if (tmp < min or ((tmp == min) and (random.randint(0, 1000) % 2 == 0))):
                        min = tmp
                    board[i][j] = 0

        return min
