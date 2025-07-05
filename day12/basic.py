# フォード・ファルカーソン法での実装

def dfs_ff(s, e, flow):
    if s == e:
        return flow
    visited[s] = True
    for i in range(N): # 全てのノードを調べる
        if not visited[i] and capasity[s][i] > 0: # 未訪問かつ容量が残っている時
            f = dfs_ff(i, e, min(flow, capasity[s][i])) # 再帰的に、flowと容量の小さい方を選ぶ
            if f > 0:
                capasity[s][i] -= f # 順方向の容量を減らす
                capasity[i][s] += f # 逆方向の容量を増やす
                return f
    return 0


N, M = map(int, input().split())
capasity = [[0] * N for _ in range(N)]

for _ in range(M):
    u, v, c = map(int, input().split())
    capasity[u-1][v-1] += c

max_flow = 0
while True:
    visited = [False]*N
    f = dfs_ff(0, N-1, float('inf'))
    if not f:
        break
    max_flow += f
print(max_flow)