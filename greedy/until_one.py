n, k = map(int, input().split())

result = 0
while True:
    if n % k == 0:
        n //= k
        result += 1
    else:
        dif = n - n // k * k
        n -= dif
        result += dif

    if n == 1:
        break

print(result)
