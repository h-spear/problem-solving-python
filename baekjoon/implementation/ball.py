# https://www.acmicpc.net/problem/1547

m = int(input())
cup = [i for i in range(4)]


def change(c1, c2):
    pos1 = cup.index(c1)
    pos2 = cup.index(c2)
    cup[pos1], cup[pos2] = cup[pos2], cup[pos1]


for _ in range(m):
    a, b = map(int, input().split())
    change(a, b)

print(cup[1])
