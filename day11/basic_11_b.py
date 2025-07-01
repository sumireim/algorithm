import heapq
from collections import defaultdict

def topological_sort(N, edges):
    G = defaultdict(list)
    in_degree = [0] * N

    # グラフ構築
    for u, v in edges:
        G[u].append(v)
        in_degree[v] += 1

    # 入次数0の頂点を最小ヒープに入れる
    heap = [i for i in range(N) if in_degree[i] == 0]
    heapq.heapify(heap)

    result = []

    while heap:
        node = heapq.heappop(heap)
        result.append(node)
        for neighbor in G[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, neighbor)

    if len(result) != N:
        return -1
    return result


N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b = map(int, input().split())
    edges.append((a, b))
result = topological_sort(N, edges)
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result))) 