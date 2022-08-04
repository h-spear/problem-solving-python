# https://school.programmers.co.kr/learn/courses/30/lessons/92344
# brute force 효율성 통과 x
# https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/#%EB%AC%B8%EC%A0%9C-6-%ED%8C%8C%EA%B4%B4%EB%90%98%EC%A7%80-%EC%95%8A%EC%9D%80-%EA%B1%B4%EB%AC%BC
# 누적합 효율적으로 사용하는 방법


def solution(board, skill):
    n = len(board)
    m = len(board[0])
    temp = [[0] * m for _ in range(n)]

    for _type, r1, c1, r2, c2, degree in skill:
        degree *= -1 if _type == 1 else 1
        temp[r1][c1] += degree

        if r2 + 1 < n:
            temp[r2 + 1][c1] -= degree
        if c2 + 1 < m:
            temp[r1][c2 + 1] -= degree
        if r2 + 1 < n and c2 + 1 < m:
            temp[r2 + 1][c2 + 1] += degree

    for i in range(n):
        for j in range(1, m):
            temp[i][j] += temp[i][j - 1]

    for j in range(m):
        for i in range(1, n):
            temp[i][j] += temp[i - 1][j]

    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + temp[i][j] > 0:
                answer += 1

    return answer
