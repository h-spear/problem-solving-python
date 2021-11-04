# https://www.acmicpc.net/problem/1212

num = list(input())
binary = ["000", "001", "010", "011", "100", "101", "110", "111"]

for i, x in enumerate(num):
    if i == 0:
        print(int(binary[int(x)]), end="")
    else:
        print(binary[int(x)], end="")
