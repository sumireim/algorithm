def WarshallFloyd(V, e_list):
    INF = float('inf')
    dist = [[INF] * V for _ in range(V)]
    for i in range(V):
        dist[i][i] = 0

    for u in range(V):
        for v, cost in e_list[u]:
            dist[u][v] = cost

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist



N, M = map(int, input().split())
e_list = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if a != b:
        e_list[a].append([b, c])

Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

result = WarshallFloyd(N, e_list)

for s, g in queries:
    d = result[s][g]
    print(d if d != float('inf') else "INF")
