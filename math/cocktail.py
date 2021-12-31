# https://www.acmicpc.net/problem/21312


def taste(ts: list) -> int:
    odd = []
    even = []
    answer = 1
    for t in ts:
        if t % 2 == 0:
            even.append(t)
        else:
            odd.append(t)

    if len(odd) == 0:
        for x in even:
            answer *= x
    else:
        for x in odd:
            answer *= x
    return answer


print(taste(list(map(int, input().split()))))
