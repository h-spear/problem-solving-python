# https://www.acmicpc.net/problem/9576


def dfs(i):
    if visit[i]:
        return False
    visit[i] = 1

    for b in student[i]:
        if not book[b] or dfs(book[b]):
            book[b] = i
            return True

    return False


n, m, answer = 0, 0, 0
student, book, visit = None, None, None

for tc in range(int(input())):
    answer = 0
    n, m = map(int, input().split())
    student = [None] * (m + 1)
    book = [0] * (n + 1)
    for i in range(1, m + 1):
        a, b = map(int, input().split())
        student[i] = list(range(a, b + 1))

    for i in range(1, m + 1):
        visit = [0] * (m + 1)
        if dfs(i):
            answer += 1

    print(answer)
