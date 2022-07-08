# https://www.acmicpc.net/problem/7490


def dfs(n, numstr="1", i=2):
    global answer
    if i == n + 1:
        res = eval(numstr.replace(" ", ""))
        if not res:
            answer.append(numstr)
        return

    dfs(n, numstr + "+" + str(i), i + 1)
    dfs(n, numstr + "-" + str(i), i + 1)
    dfs(n, numstr + " " + str(i), i + 1)


for tc in range(int(input())):
    answer = []
    n = int(input())

    dfs(n)
    answer.sort()
    for x in answer:
        print(x)
    print()
