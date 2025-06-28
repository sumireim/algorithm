from collections import deque

def dfs(edges, start, end, visited): # 深さ優先探索
    if start == end: # 目的地に到達した場合
        return True
    visited[start] = True # 訪問済みにする
    for next_node in edges[start]: # 隣接ノードを探索
        if not visited[next_node]:
            if dfs(edges, next_node, end, visited): # 再帰的に探索
                return True
    return False
    
N, M, S, T = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = (int, input().split())
    edges[a-1].append(b-1) # サイズを補正
    edges[b-1].append(a-1) # サイズを補正
    
visited = [False] * N

if dfs(edges, S, T, visited):
    print("Yes")
else:
    print("No")