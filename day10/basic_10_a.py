import heapq

def dijkstra_heap(V, e_list, start):
    INF = float('inf')
    done = [False] * V # ノードの最短距離が確定済みかどうか
    dist = [INF] * V # 各ノードへの最短距離を記録
    dist[start] = 0
    node_heap = [] # ヒープ [[最短距離], [ノード番号]]
    heapq.heappush(node_heap, [0, start]) # 始点

    while node_heap:
        tmp = heapq.heappop(node_heap)
        cur_dist, cur_node = tmp[0], tmp[1]
        if done[cur_node]: # 最短距離が確定している場合
            continue
        done[cur_node] = True # 最短距離が確定したので更新
        for next_node, weight in e_list[cur_node]: # 隣接ノードを探索
            if dist[next_node] > dist[cur_node] + weight: # より短い距離が見つかった場合
                dist[next_node] = dist[cur_node] + weight # 最短距離を更新
                heapq.heappush(node_heap, [dist[next_node], next_node])
    return dist

N, M, S = map(int, input().split())
e_list = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if a != b:
        e_list[a].append([b, c])
result = dijkstra_heap(N, e_list, S)
for i in range(N):
    if result[i] == float('inf'):
        print("INF")
    else:
        print(result[i])


