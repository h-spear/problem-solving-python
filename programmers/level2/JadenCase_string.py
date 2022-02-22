# https://programmers.co.kr/learn/courses/30/lessons/12951
# title 함수 사용시 맨 앞 글자만 대문자로 변경함
# print("5sdfassdfasdASDASDdf".title())
# 해당 문제에서는 사용할 수 없음


def solution(s):
    arr = list(s)
    if arr[0].isdigit() == False and arr[0] != " ":
        arr[0] = arr[0].upper()

    for i in range(1, len(arr)):
        if arr[i] == " ":
            continue

        if arr[i - 1] == " ":
            arr[i] = arr[i].upper()
        else:
            arr[i] = arr[i].lower()
    return "".join(arr)
