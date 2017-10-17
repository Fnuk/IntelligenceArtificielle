import datetime
from __future__ import division


class MonteCarlo(object):
    def __init__(self, board, **kwargs):
        self.board = board
        self.states = []
        seconds = kwargs.get('time', 30)
        self.calculation_time = datetime.timedelta(seconds=seconds)
        self.max_moves = kwargs.get('max_moves', 100)
        #On garde pour les statistiques :
        self.wins = {} #On "sauvegarde" le nombre de parties gagnées
        self.plays = {} #On "sauvegarde" le nombre de partie jouées

    def update(self, state):
        self.states.append(state)

    def get_play(self):
        begin = datetime.datetime.utcnow()
        while datetime.datetime.utcnow() - begin < self.calculation_time:
            self.run_simulation()

        # Bail out early if there is no real choice to be made.
        if not legal:
            return
        if len(legal) == 1:
            return legal[0]

    def run_simulation(self):
        visited_states = set() #Initialisation d'un set (vide ici)
        states_copy = self.states[:] #récupère toutes les occurences du tableau
        state = states_copy[-1] #récupère la dernière occurence du tableau
        player = self.board.current_player(state)

        expand = True
        
        for t in range(self.max_moves):
            legal = self.board.legal_plays(states_copy)

            play = choice(legal)
            state = self.board.next_state(state, play)
            states_copy.append(state)

            # `player` here and below refers to the player
            # who moved into that particular state.
            if expand and (player, state) not in self.plays:
                expand = False
                self.plays[(player, state)] = 0
                self.wins[(player, state)] = 0

            visited_states.add((player, state))

            winner = self.board.winner(states_copy)
            if winner:
                break

        for player, state in visited_states:
            if (player, state) not in self.plays:
                continue
            self.plays[(player, state)] += 1
            if player == winner:
                self.wins[(player, state)] += 1