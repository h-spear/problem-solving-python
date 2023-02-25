n, m, k = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort(reverse=True)
number = 0

while m:
    if m >= k:
        number += lst[0] * k
        m -= k
    else:
        number += lst[0] * m
        break

    number += lst[1]
    m -= 1

print(number)
