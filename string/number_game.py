# https://www.acmicpc.net/problem/1755

_dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

li = []
m, n = map(int, input().split())
for i in range(m, n + 1):
    s = str(i)
    temp = ""
    for numchar in s:
        temp += _dict[numchar]
        temp += " "
    li.append((temp, i))

li.sort()
for i, (read, num) in enumerate(li):
    print(num, end=" ")
    if (i + 1) % 10 == 0:
        print()
