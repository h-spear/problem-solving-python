def solution(n, lost, reserve):
    reserve.sort()
    for i, x in enumerate(reserve):
        if x not in lost:
            continue
        lost.remove(x)
        reserve[i] = -1

    for x in reserve:
        if x == -1:
            continue
        for _x in [x - 1, x + 1]:
            if _x not in lost:
                continue
            lost.remove(_x)
            break

    return n - len(lost)
