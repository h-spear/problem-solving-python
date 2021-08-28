# https://www.acmicpc.net/problem/5430

import sys
from collections import deque

for _ in range(int(input().rstrip())):
    input = sys.stdin.readline

    commands = list(input().rstrip())
    n = int(input().rstrip())
    input_data = input().rstrip()
    if input_data[0] == "[" and input_data[1] == "]":
        array = list()
    else:
        array = input_data[1:-1].split(",")

    array_reverse = deque(reversed(array))
    array = deque(array)

    error = False
    reverse = False
    for cmd in commands:
        if cmd == "R":
            reverse = not reverse
        elif cmd == "D":
            if len(array) == 0:
                error = True
                break
            if reverse:
                array.pop()
                array_reverse.popleft()
            else:
                array.popleft()
                array_reverse.pop()

    if error:
        print("error")
    else:
        print("[", ",".join((array if not reverse else array_reverse)), "]", sep="")
