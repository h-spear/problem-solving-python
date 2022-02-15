# https://www.acmicpc.net/problem/1414

num_hash = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

n = int(input())
edges = []
parent = [i for i in range(n)]
answer = 0
for i in range(n):
    str = list(input())
    for j in range(len(str)):
        if str[j] == "0":
            continue
        numedges.append((_hash[str[j]], i, j))
        numanswer += _hash[str[j]]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def kruskal():
    global answer
    edges.sort()

    for cost, x, y in edges:
        if find(parent, x) == find(parent, y):
            continue
        answer -= cost
        union(parent, x, y)

    for i in range(n):
        find(parent, i)

    if sum(parent) == 0:
        print(answer)
    else:
        print(-1)


kruskal()
