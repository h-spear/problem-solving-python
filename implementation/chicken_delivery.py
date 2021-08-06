# https://www.acmicpc.net/problem/15686

from itertools import combinations

n, m = map(int, input().split())

stores = []
houses = []

def chicken_distance(house_pos, stores):
  result = 10000;
  for store_pos in stores:
    dist_r = abs(house_pos[0]-store_pos[0])
    dist_c = abs(house_pos[1]-store_pos[1])
    result = min(result, dist_r + dist_c)
  return result

for r in range(n):
  input_data = list(map(int, input().split()))
  for c in range(n):
    if input_data[c] == 1:
      houses.append((r+1,c+1))
    elif input_data[c] == 2:
      stores.append((r+1,c+1))

store_select_cases = combinations(stores,m)

answer = 100000000
for case in store_select_cases:
  distance = 0
  for house in houses:
    distance += chicken_distance(house, case)
  answer = min(answer, distance)

print(answer)