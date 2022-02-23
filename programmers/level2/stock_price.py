# https://programmers.co.kr/learn/courses/30/lessons/42584/


def solution(prices):
    answer = []
    for i, price in enumerate(prices):
        for j in range(i + 1, len(prices)):
            if prices[j] < price or j == len(prices) - 1:
                answer.append(j - i)
                break
    answer.append(0)
    return answer


# 스택(훨씬 효율적)
def solution(prices):
    l = len(prices)
    answer = [i for i in range(l - 1, -1, -1)]
    stack = []
    for i in range(l):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
