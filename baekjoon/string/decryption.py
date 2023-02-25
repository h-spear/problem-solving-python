# https://www.acmicpc.net/problem/9046

from collections import Counter

for tc in range(int(input())):
    top2 = Counter(input().replace(" ", "")).most_common(2)

    if len(top2) >= 2 and top2[0][1] == top2[1][1]:
        print("?")
    else:
        print(top2[0][0])
