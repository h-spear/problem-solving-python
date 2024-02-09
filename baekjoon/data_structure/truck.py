# https://www.acmicpc.net/problem/13335

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def main():
    n, w, L = map(int, input().split())
    a = list(map(int, input().split()))
    bridge = deque([0] * w)
    wgh = 0
    answer = 0
    
    for x in a:
        while True:
            answer += 1
            wgh -= bridge.popleft()
            bridge.append(0)
            if (wgh + x <= L):
                break
            
        bridge[-1] = x
        wgh += x
            
    while wgh > 0:
        wgh -= bridge.popleft()
        answer += 1
        
    print(answer)
        

if __name__ == '__main__':
    main()
    