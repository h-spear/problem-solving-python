# https://school.programmers.co.kr/learn/courses/30/lessons/49995


def solution(cookie):
    n = len(cookie)
    psum = [cookie[0]]
    for i in range(1, n):
        psum.append(psum[-1] + cookie[i])
    psum.append(0)

    answer = 0
    for l in range(n):
        flag = False  # 최적화1
        for r in range(n - 1, l, -1):
            if (psum[r] - psum[l - 1]) & 1:  # 최적화2: 합계가 홀수면 확인 X
                continue
            left = l
            right = r
            while left <= right:
                mid = (left + right) // 2
                first = psum[mid] - psum[l - 1]
                second = psum[r] - psum[mid]

                if first == second:
                    answer = max(answer, first)
                    flag = True
                    break
                elif first > second:
                    right = mid - 1
                else:
                    left = mid + 1
            if flag:
                break

    return answer
