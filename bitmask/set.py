# https://www.acmicpc.net/problem/11723
import sys

input = lambda: sys.stdin.readline().rstrip()


def func(params):
    global bits
    x = 0
    if len(params) == 2:
        x = int(params[1])
    if params[0] == "add":
        bits |= 1 << x
    elif params[0] == "remove":
        bits &= ~(1 << x)
    elif params[0] == "check":
        print(1 if bits & (1 << x) else 0)
    elif params[0] == "toggle":
        bits ^= 1 << x
    elif params[0] == "all":
        bits = (1 << 21) - 1
    elif params[0] == "empty":
        bits = 0


m = int(input())
bits = 0

for _ in range(m):
    params = input().split()
    func(params)
