# https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

# value로 key를 찾을 때 딕셔너리는 전체를 순회하면서 비효율적
# 시간 절약을 위해 key:value, value:key 딕셔너리 두개 생성
pocketmon_num = dict()
pocketmon_name = dict()

for i in range(1,n+1):
  name = input().rstrip()
  pocketmon_num[i] = name
  pocketmon_name[name ] =  i

for _ in range(m):
  cmd = input().rstrip()
  if cmd.isdigit():
    print(pocketmon_num[int(cmd)])
  else:
    print(pocketmon_name[cmd])