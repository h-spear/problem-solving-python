# https://programmers.co.kr/learn/courses/30/lessons/17677


def solution(str1, str2):
    basket = [[] for _ in range(2)]
    for idx, string in enumerate([str1, str2]):
        for i in range(0, len(string) - 1):
            elem = string[i : i + 2].lower()
            if (ord(elem[0]) < ord("a") or ord(elem[0]) > ord("z")) or (
                ord(elem[1]) < ord("a") or ord(elem[1]) > ord("z")
            ):
                continue
            basket[idx].append(elem)

    basket[0].sort()
    basket[1].sort()
    cnt = 0
    i, j = 0, 0
    while i < len(basket[0]) and j < len(basket[1]):
        if basket[0][i] == basket[1][j]:
            cnt += 1
            i += 1
            j += 1
        elif basket[0][i] < basket[1][j]:
            i += 1
        else:
            j += 1

    if len(basket[0]) == 0 and len(basket[1]) == 0:
        return 65536

    similarity = cnt / (len(basket[0]) + len(basket[1]) - cnt)
    return int(65536 * similarity)
