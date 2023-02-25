# https://www.acmicpc.net/problem/20546


def bnp(cash, stock):
    cnt = 0
    for s in stock:
        if cash >= s:
            cnt += cash // s
            cash = cash % s
    return stock[-1] * cnt + cash


def threethree(cash, stock):
    down = 0
    up = 0
    cnt = 0
    for i in range(1, len(stock)):
        if stock[i - 1] > stock[i]:
            up = 0
            down += 1
            if down >= 3:
                cnt += cash // stock[i]
                cash = cash % stock[i]
        elif stock[i - 1] < stock[i]:
            down = 0
            up += 1
            if up >= 3:
                cash += cnt * stock[i]
                cnt = 0
    return stock[-1] * cnt + cash


cash = int(input())
stock = list(map(int, input().split()))
_bnp = bnp(cash, stock)
_threethree = threethree(cash, stock)

if _bnp < _threethree:
    print("TIMING")
elif _bnp > _threethree:
    print("BNP")
else:
    print("SAMESAME")
