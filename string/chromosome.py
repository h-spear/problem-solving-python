# https://www.acmicpc.net/problem/9342

import re

pattern = re.compile("^[A-F]?A+F+C+[A-F]?$")
for tc in range(int(input())):
    string = input()
    if re.match(pattern, string):
        print("Infected!")
    else:
        print("Good")
