def EvaluationFunction(plateau, position, joueur):
    val = 0
    # premier coup ? milieu !
    if plateau.count("0") == 121:
        if position[0] == position[1] == 5:
            val += 4
    # test si bridge
    # retourne entre 0 (bridge tous adverses) et 12/14 (bridge tous à nous)
    val += bridge(plateau, position, joueur)
    # test si echelle
    # retourne entre 0 et 
    val += ladder(plateau, position, joueur)
    return val


def bridge(plateau, position, joueur):
    val = 0
    # bridge vertical
    if plateau[position[0] + 1, position[1] - 2] == joueur:
        if joueur == -1:
            val += 3
        else:
            val += 2
    if plateau[position[0] - 1, position[1] + 2] == joueur:
        if joueur == -1:
            val += 3
        else:
            val += 2
    if plateau[position[0] + 1, position[1] - 2] == 0:
        if joueur == -1:
            val += 2
        else:
            val += 1
    if plateau[position[0] - 1, position[1] + 2] == 0:
        if joueur == -1:
            val += 2
        else:
            val += 1
    # bridge /
    if plateau[position[0] + 2, position[1] - 1] == joueur:
        val += 2
    if plateau[position[0] - 2, position[1] + 1] == joueur:
        val += 2
    if plateau[position[0] + 2, position[1] - 1] == 0:
        val += 1
    if plateau[position[0] - 2, position[1] + 1] == 0:
        val += 1
    # bridge \
    if plateau[position[0] - 1, position[1] - 1] == joueur:
        val += 2
    if plateau[position[0] + 1, position[1] + 1] == joueur:
        val += 2
    if plateau[position[0] - 1, position[1] - 1] == 0:
        val += 1
    if plateau[position[0] + 1, position[1] + 1] == 0:
        val += 1
    return val


def ladder(plateau, position, joueur):
    val = 0
    return val
