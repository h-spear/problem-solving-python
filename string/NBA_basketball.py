# https://www.acmicpc.net/problem/2852


def calc_time(t1, t2):
    m1, s1 = t1.split(":")
    m2, s2 = t2.split(":")
    return int(m2) * 60 + int(s2) - int(m1) * 60 - int(s1)


def expression_time(seconds):
    m = str(seconds // 60)
    seconds = str(seconds % 60)
    print("{}:{}".format((2 - len(m)) * "0" + m, (2 - len(seconds)) * "0" + seconds))


score = [(0, "00:00")]
n = int(input())
one, two = 0, 0
for _ in range(n):
    team, t = input().split()
    team = int(team)
    if team == 1:
        one += 1
        if one > two:
            score.append((1, t))
    else:
        two += 1
        if two > one:
            score.append((2, t))

    if two == one:
        score.append((0, t))

score.append((0, "48:00"))

answer = [0, 0]
for i in range(len(score) - 1):
    team, t = score[i]
    if team == 0:
        continue
    next_t = score[i + 1][1]
    time = calc_time(t, next_t)

    if team == 1:
        answer[0] += time
    else:
        answer[1] += time

for t in answer:
    expression_time(t)
