# https://www.acmicpc.net/problem/3005

r, c = map(int, input().split())
words = []
puzzle = []
for _ in range(r):
    input_data = input()
    puzzle.append(input_data)
    if "#" in input_data:
        candidates = input_data.split("#")
        for candidate in candidates:
            if len(candidate) <= 1:
                continue
            words.append(candidate)
    else:
        words.append(input_data)

for j in range(c):
    tmp = ""
    for i in range(r):
        tmp += puzzle[i][j]
    if "#" in tmp:
        candidates = tmp.split("#")
        for candidate in candidates:
            if len(candidate) <= 1:
                continue
            words.append(candidate)
    else:
        words.append(tmp)

words.sort()
print(words[0])
