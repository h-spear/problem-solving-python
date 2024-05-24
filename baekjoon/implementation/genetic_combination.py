# https://www.acmicpc.net/problem/25758

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline()


def main():
    input()
    counter = defaultdict(int)
    gene = []
    for g in list((input().split())):
        if counter[g] < 2:
            counter[g] += 1
            gene.append(g)

    N = len(gene)
    bucket = set()
    for i in range(N):
        for j in range(i + 1, N):
            bucket.add(gene[i][0] if gene[i][0] > gene[j][1] else gene[j][1])
            bucket.add(gene[j][0] if gene[j][0] > gene[i][1] else gene[i][1])

    print(len(bucket))
    print(" ".join(sorted(list(bucket))))


if __name__ == "__main__":
    main()
