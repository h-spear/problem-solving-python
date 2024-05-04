# https://www.acmicpc.net/problem/1270

from collections import defaultdict


def main():
    n = int(input())
    for _ in range(n):
        t, *soldiers = list(map(int, input().split()))
        counter = defaultdict(int)
        max_solider = -1
        for soldier in soldiers:
            counter[soldier] += 1
            max_solider = max(max_solider, counter[soldier])

        filtered = list(filter(lambda x: x[1] == max_solider, counter.items()))
        if max_solider > t / 2 and len(filtered) == 1:
            print(filtered[0][0])
        else:
            print("SYJKGW")


if __name__ == "__main__":
    main()
