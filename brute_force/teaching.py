from itertools import combinations

n, k = map(int, input().split())
words = []
for _ in range(n):
    words.append(
        set(
            input()
            .replace("a", "")
            .replace("n", "")
            .replace("t", "")
            .replace("i", "")
            .replace("c", "")
        )
    )

if k < 5:
    print(0)
    exit()

teach = set()
for word in words:
    teach = teach | word

answer = 0
for li in combinations(teach, min(k - 5, len(teach))):
    S = set(li)
    cnt = 0
    for word in words:
        if len(word - S) == 0:
            cnt += 1

    answer = max(answer, cnt)

print(answer)
