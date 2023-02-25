N = int(input())


def hasThree(num):
    ones = num % 10
    tens = num // 10
    if tens == 3 or ones == 3:
        return True
    return False


result = 0
for h in range(0, N + 1):
    for m in range(0, 60):
        for s in range(0, 60):
            if hasThree(h) or hasThree(m) or hasThree(s):
                result += 1

print(result)
