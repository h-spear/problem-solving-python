# https://www.acmicpc.net/problem/1074

n,r,c= map(int, input().split())

cnt = 0
while n != 1:
  if r >= 2**(n-1):
    cnt += 2**(2*n-1)
    r -= 2 ** (n-1)


  if c >= 2**(n-1):
    cnt += 2**(2*n-2)
    c -= 2 ** (n-1)
  
  n -= 1
  
print(cnt+2*r+c)
