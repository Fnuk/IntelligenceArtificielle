

class Player (object):

     def move(self, board, player):

          first_play = True

          for a in range(11):
               if(board[a].count(1) or board[a].count(-1) ):
                    first_play = False

          if(first_play):
               board[5][5] = player
          else:
               i = 0
               j = 0
               while board[i][j] != 0 or (i==10 and j==10):
                    if(player == 1):
                         j += 1
                         if j > 10:
                              j = 0
                              i += 1
                    else :
                         i += 1
                         if i > 10:
                              i = 0
                              j += 1

                    print("position jouée :"+i+", "+j)

