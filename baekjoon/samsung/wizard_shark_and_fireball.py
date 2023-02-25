# https://www.acmicpc.net/problem/20056

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
n, m, k = map(int, input().split())

balls = []
for _ in range(m):
    ball_info = list(map(int, input().split()))
    ball_info[0] -= 1
    ball_info[1] -= 1
    balls.append(ball_info)

# 0 1 2 3 4 5 6 7
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def one_order():
    global balls
    _dict = defaultdict(list)
    while balls:
        r,c,m,s,d = balls.pop()
        nx = (r + s* dx[d] + n) % n
        ny = (c + s* dy[d] + n) % n
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        _dict[(nx,ny)].append((nx,ny,m,s,d))
    
    for balls_in_coord in _dict.values():
        if len(balls_in_coord) == 1:
            balls.append(balls_in_coord[0])
            continue
        
        
        _r,_c, _m, _s = 0,0,0,0
        d_odd,d_even = 0,0
        for r,c,m,s,d in balls_in_coord:
            _r = r
            _c = c
            _m += m
            _s += s
            
            if d % 2 == 0:
                d_even += 1
            else:
                d_odd += 1
        
        _m //=5
        _s //= len(balls_in_coord)
        
        if _m == 0:
            continue
        
        if d_odd == 0 or d_even == 0:
            for _d in [0,2,4,6]:
                balls.append((_r,_c,_m,_s,_d))
        else:
            for _d in [1,3,5,7]:
                balls.append((_r,_c,_m,_s,_d))
                
def mass_sum():
    sum = 0
    for _, _, m, _,_ in balls:
        sum += m
    return sum

for _ in range(k):
    one_order()
print(mass_sum())