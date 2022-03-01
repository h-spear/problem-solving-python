import functools

# reduce
a = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(a)


# cmp_to_key
# 정렬 기준 custom
# https://programmers.co.kr/learn/courses/30/lessons/42746
# compare 함수의 return 값 >= 0 : a, b의 순서 변경
#                           else: 순서 유지
def compare(a, b):
    if int(a + b) < int(b + a):
        return 1  # 0 or 양수 : a, b의 순서를 변경
    return -1  # 음수 : 순서 유지


numbers = list(map(str, [3, 30, 34, 5, 9]))
numbers.sort(key=functools.cmp_to_key(compare))
answer = "".join(numbers)
print("0" if answer[0] == "0" else answer)
