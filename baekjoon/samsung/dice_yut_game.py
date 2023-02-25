# https://www.acmicpc.net/problem/17825

red_path = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 6,
    6: 7,
    7: 8,
    8: 9,
    9: 10,
    10: 11,
    11: 12,
    12: 13,
    13: 14,
    14: 15,
    15: 16,
    16: 17,
    17: 18,
    18: 19,
    19: 20,
    20: 21,
    21: 21,  ####### 도착점에서는 더 이상 이동X
    22: 23,
    23: 24,
    24: 25,
    28: 27,
    27: 26,
    26: 25,
    25: 31,
    29: 30,
    30: 25,
    31: 32,
    32: 20,
}
blue_path = {
    5: 22,
    10: 29,
    15: 28,
}

score = {
    0: 0,
    1: 2,
    2: 4,
    3: 6,
    4: 8,
    5: 10,
    6: 12,
    7: 14,
    8: 16,
    9: 18,
    10: 20,
    11: 22,
    12: 24,
    13: 26,
    14: 28,
    15: 30,
    16: 32,
    17: 34,
    18: 36,
    19: 38,
    20: 40,
    21: 0,  # 도착점
    22: 13,
    23: 16,
    24: 19,
    25: 25,
    26: 26,
    27: 27,
    28: 28,
    29: 22,
    30: 24,
    31: 30,
    32: 35,
}

dice = list(map(int, input().split()))
pos = [0, 0, 0, 0]
answer = 0


def simul(i=0, summation=0):
    global answer
    if i == 10:
        answer = max(answer, summation)
        return

    used = set()
    for idx, p in enumerate(pos):
        dice_num = dice[i]
        now = p

        if now in used:
            continue
        if now == 21:
            continue

        used.add(now)

        if now in blue_path:
            now = blue_path[now]
            dice_num -= 1

        for _ in range(dice_num):
            now = red_path[now]

        if now != 21 and now in pos:
            continue

        pos[idx] = now
        simul(i + 1, summation + score[now])
        pos[idx] = p


simul()
print(answer)
