def EvaluationFunction(plateau, position, joueur):
    if bridge(plateau, position, joueur):
        return;


def bridge(plateau, position, joueur):
    val = 0
    if joueur == -1:
        if plateau[position[0] + 1, position[1] - 2] == joueur:
            val += 4
        elif plateau[position[0] + 1, position[1] - 2] == 0
            val += 2

    return val
