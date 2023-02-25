# https://www.acmicpc.net/problem/2224

num_hash = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
    "a": 27,
    "b": 28,
    "c": 29,
    "d": 30,
    "e": 31,
    "f": 32,
    "g": 33,
    "h": 34,
    "i": 35,
    "j": 36,
    "k": 37,
    "l": 38,
    "m": 39,
    "n": 40,
    "o": 41,
    "p": 42,
    "q": 43,
    "r": 44,
    "s": 45,
    "t": 46,
    "u": 47,
    "v": 48,
    "w": 49,
    "x": 50,
    "y": 51,
    "z": 52,
}
alpha_hash = {v: k for k, v in num_hash.items()}
n = int(input())
graph = [[0] * 53 for _ in range(53)]
for _ in range(n):
    P, Q = input().split(" => ")
    a, b = num_hash[P], num_hash[Q]
    graph[a][b] = 1


def floyd_warshall():
    for k in range(1, 53):
        for i in range(1, 53):
            for j in range(1, 53):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1

    answer = []
    for i in range(1, 53):
        for j in range(1, 53):
            if i == j:
                continue
            if graph[i][j] == 1:
                answer.append("{0} => {1}".format(alpha_hash[i], alpha_hash[j]))

    print(len(answer))
    for x in sorted(answer):
        print(x)


floyd_warshall()
