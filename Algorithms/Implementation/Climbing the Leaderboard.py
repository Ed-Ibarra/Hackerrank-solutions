def climbingLeaderboard(leaderboard, scores):
    # unique_scores = list(set(leaderboard))
    # positions = []
    #
    # for i in range(len(scores)):
    #     unique_scores.append(scores[i])
    #     positions.append(sorted(unique_scores, reverse=True).index(scores[i]) + 1)

    # puntuaciones del jugador nuevo que no estan en la leaderboard
    set_diff = set(scores) - set(leaderboard)
    print(f"set_diff = {set_diff}")

    # unir las puntuaciones del jugador a la leaderboard
    merged = set(leaderboard) | set(scores)
    print(f"union = {merged}")

    # hacer un diccionario con la union final de puntuaciones y su posicion
    merged = {v: k for k, v in dict(enumerate(sorted(merged, reverse=True), start=1)).items()}
    print(f"diccionario {merged}\n")
    results = []

    # por cada Puntuacion en [5, 25, 50, 120]
    for p in scores:
        print("")
        # si la Puntuacion esta en set_diff {120, 25, 5}
        if p in set_diff:
            # elimina la Puntuacion de set_diff
            print(f"si {p} in set_diff.....remove{p}")
            set_diff.remove(p)
            # set_diff {120, 25}   ->  len() = 2

        print(f"p = {p}    merged[p] = {merged[p]} - {len(set_diff)}")
        # append(posicion segun el puntaje - len(set_diff))
        results.append(merged[p] - len(set_diff))

    return results

if __name__ == '__main__':

    _ = int(input())
    # Leaderboard
    leaderboard = list(map(int, input().split()))

    _ = int(input())
    # Scores gotten by player
    scores = list(map(int, input().split()))

    print(*climbingLeaderboard(leaderboard, scores), sep="\n")




"""

Leaderboard
100 100 50 40 40 20 10

There are 7 players, based in their scores, the leaderboard it'll be the following,
(PLEASE, IGNORE COLUMN "NAME" IT'S JUST FOR VISUAL HELP):
Rank | Name | Score
 1   |  A   |  100
 1   |  B   |  100
 2   |  C   |   50
 3   |  D   |   40
 3   |  E   |   40
 4   |  F   |   20
 5   |  G   |   10
 




Player scores
5 25 50 120



7
100 100 50 40 40 20 10
4
5 25 50 120

"""