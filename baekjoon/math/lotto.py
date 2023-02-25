# https://www.acmicpc.net/problem/6603

from itertools import combinations

data = []
while True:
    input_data = list(map(int, input().split()))
    if input_data == [0]:
        break
    data.append(input_data)

for lotto in data:
    for array in combinations(lotto[1:], 6):
        for x in array:
            print(x, end=" ")
        print()
    print()
