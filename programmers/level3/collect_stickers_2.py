def solution(sticker):

    n = len(sticker)
    if n <= 2:
        return max(sticker)

    # select first:
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    # no select first
    dp2 = [0] * n
    dp2[1] = sticker[1]
    dp2[2] = max(sticker[1], sticker[2])
    for i in range(3, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(dp1[n - 2], dp2[n - 1])
