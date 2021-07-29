n, m, k = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort(reverse=True)
number = 0

count = int(m/(k+1)) * k
count += m % (k+1)

number += count * lst[0]
number += (m - count) * lst[1]

print(number)
