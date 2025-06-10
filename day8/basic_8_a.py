
N, W = map(int, input().split())
items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))
    
max_value = sum(v for _, v in items)
INF = 10**15

dp = [INF] * (max_value + 1)
dp[0] = 0 

for w, v in items:
    for val in range(max_value - v, -1, -1):
        if dp[val] != INF and dp[val] + w <= W:
            dp[val + v] = min(dp[val + v], dp[val] + w)

ans = 0
for val in range(max_value + 1):
    if dp[val] <= W:
        ans = max(ans, val)
print(ans)


''' # previous code
dp = [[-1] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    w, v = items[i - 1] 
    for j in range(W + 1):
        # choose not to take the item
        if dp[i - 1][j] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
        # choose to take the item
        if j >= w and dp[i - 1][j - w] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)
ans = max(dp[N])
print(ans)
'''