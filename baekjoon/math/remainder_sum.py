# https://www.acmicpc.net/problem/10986
# https://velog.io/@learningssik/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-10986-%ED%8C%8C%EC%9D%B4%EC%8D%AC

n, m = map(int, input().split())
a = list(map(int, input().split()))
acc_sum = [0] * n
mod_cnt = [0] * m
answer = 0

acc_sum[0] = a[0]
mod_cnt[acc_sum[0] % m] += 1

for i in range(1, n):
    acc_sum[i] = acc_sum[i - 1] + a[i]
    mod_cnt[acc_sum[i] % m] += 1

for x in acc_sum:
    if x % m == 0:
        answer += 1

for y in mod_cnt:
    answer += y * (y - 1) // 2

print(answer)
