# https://www.acmicpc.net/problem/17413

import re

s = input()
reversed = re.sub("[< >]", "|", s).split("|")
for i in range(len(reversed)):
    reversed[i] = reversed[i][::-1]
reversed = " ".join(reversed)

answer = ""
open = False
for i in range(len(s)):
    if s[i] == "<":
        open = True
        answer += "<"
        continue
    elif s[i] == ">":
        open = False
        answer += ">"
        continue

    if open:
        answer += s[i]
    else:
        answer += reversed[i]

print(answer)
