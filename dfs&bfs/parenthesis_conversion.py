# https://programmers.co.kr/learn/courses/30/lessons/60058


def findBalance(string):
    count = 0
    for i in range(0, len(string)):
        if string[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i + 1
    return -1


def isCorrect(string):
    count = 0
    for i in range(0, len(string)):
        if string[i] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True if count == 0 else False


def reverseBracket(string):
    converted = list(string)
    for i in range(0, len(converted)):
        if converted[i] == ")":
            converted[i] = "("
        else:
            converted[i] = ")"
    return "".join(converted)


def solution(p):
    if p == "":
        return p

    answer = ""
    boundary = findBalance(p)
    u = p[:boundary]
    v = p[boundary:]
    if isCorrect(u):
        answer += u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        answer += reverseBracket(u[1:-1])

    return answer


p = "()))((()"
print(p)
print(solution(p))
