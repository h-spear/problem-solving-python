# https://www.acmicpc.net/problem/14888

n = int(input())
numbers = list(map(int, input().split()))
operator = tuple(map(int, input().split()))

max_number = -1000000000
min_number = 1000000000

def dfs(number, operator, i):
  global max_number, min_number
  add, sub, mul, div = operator

  if i == n:
    max_number = max(max_number, number)
    min_number = min(min_number, number)
    return;

  if add != 0:
    dfs(number + numbers[i], (add-1,sub,mul,div), i+1)
  if sub != 0:
    dfs(number - numbers[i], (add,sub-1,mul,div), i+1)
  if mul != 0:
    dfs(number * numbers[i], (add,sub,mul-1,div), i+1)
  if div != 0:
    dfs(abs(number) // numbers[i] * (1 if number > 0 else -1), (add,sub,mul,div-1), i+1)
  return;

dfs(numbers[0], operator, 1)
print(max_number, min_number)
