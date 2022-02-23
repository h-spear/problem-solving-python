# https://programmers.co.kr/learn/courses/30/lessons/77885


def solution(numbers):
    answer = []
    for number in numbers:
        number = int(number)
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            idx = -1
            for i, x in enumerate(reversed(bin(number).replace("0b", ""))):
                if x == "0":
                    idx = i
                    break

            if idx == -1:
                i = 1
                while i < number:
                    i *= 2
                answer.append(number + i - i // 2)
            else:
                answer.append(number + 2 ** idx - 2 ** (idx - 1))

    return answer
