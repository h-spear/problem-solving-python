# https://www.acmicpc.net/problem/1283

from typing import *


def findAnswer(option: str) -> str:
    splited: List[str] = option.split()
    charIdx: int = -1

    # 1
    for i, string in enumerate(splited):
        charIdx = ord(string[0].upper()) - ord("A")
        if commandMap[charIdx] == False:
            commandMap[charIdx] = True
            splited[i] = "[" + string[0] + "]" + string[1:]
            return " ".join(splited)

    # 2
    for i, char in enumerate(option):
        if char == " ":
            continue

        charIdx = ord(char.upper()) - ord("A")
        if commandMap[charIdx] == False:
            commandMap[charIdx] = True
            return option[:i] + "[" + option[i] + "]" + option[i + 1 :]

    # 3
    return option


n: int = int(input())
options: List[str] = []
commandMap: List[bool] = [False] * 26
results: List[str] = []

for _ in range(n):
    options.append(input())

for option in options:
    print(findAnswer(option))
