# https://www.acmicpc.net/problem/16719


def fn(string, show, used):
    candidates = []
    for i in range(len(string)):
        if i in used:
            continue
        temp = ""
        show[i] = 1
        for j in range(len(string)):
            if show[j] == 1:
                temp += string[j]
        show[i] = 0
        candidates.append((temp, i))

    candidates.sort()
    char, idx = candidates[0]
    print(char)
    show[idx] = 1
    used.add(idx)


string = list(input())
show = [0] * len(string)
used = set()
for _ in range(len(string)):
    fn(string, show, used)
