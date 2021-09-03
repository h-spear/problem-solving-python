# https://www.acmicpc.net/problem/1043


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    global know
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
        know = a
    else:
        parent[a] = b
        know = b


n, m = map(int, input().split())
knows = list(map(int, input().split()))[1:]

parties = []
for _ in range(m):
    parties.append(sorted(list(map(int, input().split()))[1:]))

answer = 0

if len(knows) == 0:
    answer = m
else:
    parent = [0] * (n + 1)
    know = knows[0]
    knows = set(knows)

    for i in range(1, n + 1):
        parent[i] = i

    while True:
        revised = False
        for party in parties:
            lie = True
            for x in knows:
                if x in party:
                    lie = False
                    break

            if not lie:
                for x in party:
                    if x not in knows:
                        union(parent, x, know)
                        knows.add(x)
                        revised = True

        if not revised:
            break

    for party in parties:
        lie = True
        for x in knows:
            if x in party:
                lie = False
                break
        if lie:
            answer += 1

print(answer)
