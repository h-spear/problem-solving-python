# https://www.acmicpc.net/problem/2720

for tc in range(int(input())):
    c = int(input())
    coins = [25, 10, 5, 1]
    answer = []

    for coin in coins:
        answer.append(c // coin)
        c %= coin

    print(*answer)
