# https://programmers.co.kr/learn/courses/30/lessons/42860/
# greedy X, Bruteforce O


def solution(name):
    answer = [123456789]
    ln = len(name)
    disp = [0] * ln
    target = []

    for char in name:
        up = ord(char) - ord("A")
        down = ord("Z") - ord(char) + 1
        target.append(min(up, down))

    def dfs(disp, cursur, cnt, ans):
        if disp[cursur] != target[cursur]:
            cnt += target[cursur]
            disp[cursur] = target[cursur]

        if disp == target:
            ans[0] = min(ans[0], cnt)
            return

        for i in range(ln - 1):
            next = (cursur + i) % ln
            if disp[next] != target[next]:
                dfs(disp.copy(), next, cnt + i, ans)
                break

        for i in range(ln - 1):
            next = (cursur - i + ln) % ln
            if disp[next] != target[next]:
                dfs(disp.copy(), next, cnt + i, ans)
                break

    # bruteforce
    dfs(disp.copy(), 0, 0, answer)
    return answer[0]
