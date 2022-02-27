# https://www.acmicpc.net/problem/1972


def is_surprising(string):
    for d in range(1, len(string)):
        temp = []
        for i in range(len(string) - d):
            temp.append(string[i] + string[i + d])
        lt = len(temp)
        if len(set(temp)) != lt:
            print(string, "is NOT surprising.")
            return
    print(string, "is surprising.")


while 1:
    string = input()
    if string == "*":
        break
    is_surprising(string)
