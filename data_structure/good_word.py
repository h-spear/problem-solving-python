def is_good_word(s):
    ls = len(s)
    stack = []
    if ls & 1:
        return False

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if stack:
        return False
    else:
        return True


n = int(input())
cnt = 0
for _ in range(n):
    s = input()
    cnt += is_good_word(s)

print(cnt)
