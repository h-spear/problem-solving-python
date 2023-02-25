# https://www.acmicpc.net/problem/2004
# 참고 https://mjn9ine.tistory.com/entry/BOJ-2004-%EC%A1%B0%ED%95%A9-0%EC%9D%98-%EA%B0%9C%EC%88%98-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC?category=962929


def count_two(num):
    cnt = 0
    while num > 0:
        num = num // 2
        cnt += num
    return cnt


def count_five(num):
    cnt = 0
    while num > 0:
        num = num // 5
        cnt += num
    return cnt


n, m = map(int, input().split())
print(
    min(
        count_two(n) - count_two(m) - count_two(n - m),
        count_five(n) - count_five(m) - count_five(n - m),
    )
)
