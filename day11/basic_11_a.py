class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]
    
    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        self.parent[y_root] = x_root
        return True

# クラスカル法
def kruskal(N, edges):
    edges.sort(key=lambda x: x[2]) 
    uf = UnionFind(N)
    total_weight = 0
    for u, v, weight in edges:
        if uf.unite(u, v):
            total_weight += weight
    return total_weight


N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

result = kruskal(N, edges)
print(result)
