import math

n = int(input())
radius = list(map(int, input().split()))
first_ring = radius[0]

for idx, curr_ring in enumerate(radius):
    if idx == 0:
        continue

    _gcd = math.gcd(first_ring, curr_ring)
    print("{}/{}".format(first_ring // _gcd, curr_ring // _gcd))
