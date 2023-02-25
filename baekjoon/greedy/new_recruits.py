# https://www.acmicpc.net/problem/1946

for tc in range(int(input())):
    n = int(input())
    rank = []
    for _ in range(n):
        rank.append(tuple(map(int, input().split())))

    # 서류 성적을 기준으로 정렬
    rank.sort()

    answer = 1
    man = rank[0][1]
    for i in range(1, n):
        if man > rank[i][1]:
            man = rank[i][1]
            answer += 1

    print(answer)
