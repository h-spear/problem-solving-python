# https://www.acmicpc.net/problem/20115

n = int(input())
drink = list(map(int, input().split()))
drink.sort(reverse=True)

while len(drink) > 1:
    adder = drink.pop()
    drink[0] += adder / 2

if int(drink[0]) == drink[0]:
    print(int(drink[0]))
else:
    print(drink[0])
