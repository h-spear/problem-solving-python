# https://www.acmicpc.net/problem/10610

n = input()

if not n.count("0"):
    print(-1)
elif sum(map(int, n)) % 3:
    print(-1)
else:
    print("".join(sorted(n, reverse=True)))
