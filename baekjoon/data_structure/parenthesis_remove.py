# https://www.acmicpc.net/problem/2800

s = list(input())

stack = []
pair = dict()
expr = []

for idx, char in enumerate(s):
    if char == "(":
        stack.append(idx)
    elif char == ")":
        i = stack.pop()
        pair[idx] = i

b = [k for k in pair]
b.sort()
lb = len(b)


def dfs(i):
    close_bracket = b[i]
    open_bracket = pair[close_bracket]

    s[open_bracket] = ""
    s[close_bracket] = ""
    expr.append("".join(s))
    for j in range(i + 1, lb):
        dfs(j)
    s[open_bracket] = "("
    s[close_bracket] = ")"


for i in range(lb):
    dfs(i)

# 중복된 식을 제거해야 함.
expr = list(set(expr))
expr.sort()
for x in expr:
    print(x)
