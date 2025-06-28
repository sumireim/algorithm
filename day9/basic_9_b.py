from collections import deque

def bfs(maze, H, W, sy, sx, gy, gx):
    sy -= 1
    sx -= 1
    gy -= 1
    gx -= 1

    dist = [[-1]*W for _ in range(H)]
    dist[sy][sx] = 0

    queue = deque()
    queue.append((sy, sx))

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and maze[ny][nx] == '.' and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny, nx))

    return dist[gy][gx]

H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [input().strip() for _ in range(H)]

print(bfs(maze, H, W, sy, sx, gy, gx))
