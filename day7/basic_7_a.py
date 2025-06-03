import sys

def calc_cost(i, j, H):
    return abs(H[i] - H[j])


N = int(input())
H = list(map(int, input().split()))
dp = [0] * N
for i in range(1, N):
    if i == 1:
        dp[i] = calc_cost(0, 1, H)
    else:
        dp[i] = min(dp[i - 1] + calc_cost(i - 1, i, H), dp[i - 2] + calc_cost(i - 2, i, H))
print(dp[-1])
