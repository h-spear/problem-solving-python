# https://programmers.co.kr/learn/courses/30/lessons/67256

# 0,1,2,3,4,5,6,7,8,9,*,#
keypad = [
    (3, 1),
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 0),
    (2, 1),
    (2, 2),
    (3, 0),
    (3, 2),
]

# 두 숫자 키패드 사이의 거리
def calc_dist(num1, num2):
    x1, y1 = keypad[num1]
    x2, y2 = keypad[num2]
    return abs(x2 - x1) + abs(y2 - y1)


def solution(numbers, hand):
    answer = ""
    left, right = 10, 11
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left = number
        if number in [3, 6, 9]:
            answer += "R"
            right = number
        if number in [2, 5, 8, 0]:
            dist_left, dist_right = calc_dist(number, left), calc_dist(number, right)
            if dist_left < dist_right:
                left = number
                answer += "L"
            elif dist_left > dist_right:
                right = number
                answer += "R"
            else:
                if hand == "left":
                    answer += "L"
                    left = number
                else:
                    answer += "R"
                    right = number

    return answer
