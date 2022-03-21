# https://www.acmicpc.net/problem/17202

A = list(map(int, list(input())))
B = list(map(int, list(input())))
number = []

for i in range(8):
    number.append(A[i])
    number.append(B[i])

while len(number) > 2:
    temp = []
    for i in range(len(number) - 1):
        temp.append((number[i] + number[i + 1]) % 10)

    number = temp

print("".join(list(map(str, number))))
