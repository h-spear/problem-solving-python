# https://programmers.co.kr/learn/courses/30/lessons/42577
# 코딩테스트 고득점 Kit : hash

# sort
def solution(phone_book):
    phone_book.sort(key=lambda x: (x, len(x)))
    for i in range(len(phone_book) - 1):
        now = phone_book[i]
        if now == phone_book[i + 1][: len(now)]:
            return False
    return True


# hash
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
