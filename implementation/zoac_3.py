# https://www.acmicpc.net/problem/20436

keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
consonants = set("qwertasdfgzxcv")
vowels = set("yuiophjklbnm")


def get_distance(a, b):
    ax, ay, bx, by = 0, 0, 0, 0
    for i in range(3):
        for j in range(len(keyboard[i])):
            if keyboard[i][j] == a:
                ax, ay = i, j
            if keyboard[i][j] == b:
                bx, by = i, j
    return abs(ax - bx) + abs(ay - by)


left, right = input().split()
string = input()
answer = len(string)

for char in string:
    if char in consonants:
        answer += get_distance(left, char)
        left = char
    else:
        answer += get_distance(right, char)
        right = char

print(answer)
