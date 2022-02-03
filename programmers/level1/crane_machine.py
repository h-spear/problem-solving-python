# https://programmers.co.kr/learn/courses/30/lessons/64061


def solution(board, moves):
    n = len(board)
    answer = 0
    stack = []

    for move in moves:
        for i in range(n):
            pick = board[i][move - 1]
            if pick == 0:
                continue
            board[i][move - 1] = 0

            if stack and stack[-1] == pick:
                stack.pop()
                answer += 1
                break
            stack.append(pick)
            break

    return answer * 2
