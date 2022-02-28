# LIS(최장 증가 부분 수열, Longest Increasing Subsequence)
# 최장 증가 수열의 길이를 찾는 알고리즘
from bisect import bisect_left

# 길이를 구할 뿐 LIS를 구하지는 않음
def LIS_length(array):
    answer = 0
    dp = []
    for x in array:
        if not dp:
            dp.append(x)
            answer += 1
            continue

        if dp[-1] < x:
            dp.append(x)
            answer += 1
        else:
            index = bisect_left(dp, x)
            dp[index] = x
    return answer


# LIS를 구하는 알고리즘
def LIS(array):
    q = []
    temp = []
    for x in array:
        if not q or q[-1] < x:
            q.append(x)
            temp.append((len(q) - 1, x))
        else:
            idx = bisect_left(q, x)
            q[idx] = x
            temp.append((idx, x))

    answer = []
    now = len(q) - 1
    for i in range(len(temp) - 1, -1, -1):
        if temp[i][0] == now:
            answer.append(temp[i][1])
            now -= 1

    return sorted(answer)


# LCS(최장 공통 부분 수열, Longest Common Subsequence)

# LCS의 길이를 구하는 알고리즘(DP이용)
def LCS_length(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[m][n], dp


# LCS를 구하는 알고리즘
def LCS(word1, word2):
    # DP에서 역추적하여 LCS를 구함
    _, dp = LCS_length(word1, word2)
    i, j = len(word1), len(word2)
    answer = ""
    while i > 0 and j > 0:
        if word1[i - 1] == word2[j - 1]:
            answer += word1[i - 1]
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return answer[::-1]
