# https://www.acmicpc.net/problem/17626
# python 통과 코드
# 라그랑주의 네 제곱수 법칙(모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다)
# i, j, k for문의 범위를 줄여 시간 통과

import math
n = int(input())
result = 4
for i in range(int(math.sqrt(n)), int(math.sqrt(n//4)),-1):
  if i*i == n:
    result = 1
    break
  else:
    tmp = n - i *i
    for j in range(int(math.sqrt(tmp)), int(math.sqrt(tmp//3)), -1):
      if i*i + j*j == n:
        result = min(result, 2)
        continue
      else:
        tmp = n - i*i - j*j
        for k in range(int(math.sqrt(tmp)),int(math.sqrt(tmp//2)),-1):
          if i*i + j*j + k*k == n:
            result = min(result, 3)
print(result)