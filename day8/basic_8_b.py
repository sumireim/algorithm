INF_number = 998244353

N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    sum = [0] * (K + 1)
    for j in range(K + 1):
        sum[j] = dp[i - 1][j] if j == 0 else (sum[j - 1] + dp[i - 1][j]) % INF_number
    for j in range(K + 1):
        if j > A[i - 1]:
            dp[i][j] = (sum[j] - sum[j - A[i - 1] - 1] + INF_number) % INF_number
        else:
            dp[i][j] = sum[j]

print(dp[N][K] % INF_number)
    