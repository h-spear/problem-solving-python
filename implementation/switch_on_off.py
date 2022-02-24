# https://www.acmicpc.net/problem/1244


def male_operation(state, num):
    curr = num
    while curr < len(state):
        state[curr] = 1 - state[curr]
        curr += num


def female_operation(state, num):
    i = 1
    while num - i > 0 and num + i < len(state):
        if state[num + i] != state[num - i]:
            break
        i += 1

    for j in range(num - i + 1, num + i):
        state[j] = 1 - state[j]


num_of_switch = int(input())
state = [0]
state.extend(list(map(int, input().split())))
num_of_student = int(input())
have = []
for _ in range(num_of_student):
    gender, num = map(int, input().split())
    if gender == 1:
        male_operation(state, num)
    else:
        female_operation(state, num)

for i in range(1, num_of_switch + 1):
    print(state[i], end=" ")
    if i % 20 == 0:
        print()
