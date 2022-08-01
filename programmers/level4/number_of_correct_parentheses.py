# https://school.programmers.co.kr/learn/courses/30/lessons/12929


def solution(n):
    answer = [0]

    def func(s, op, cl):
        if op + cl == 2 * n:
            answer[0] += 1
            return

        if op > cl:
            if op + 1 <= n:
                func(s + "(", op + 1, cl)

            if cl + 1 <= n:
                func(s + ")", op, cl + 1)
        elif op == cl:
            if op + 1 <= n:
                func(s + "(", op + 1, cl)
        else:
            return

    func("", 0, 0)
    return answer[0]
