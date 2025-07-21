from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    Q = deque()
    Q.append((0, 0))
    
    dist[0][0] = 1
    visited[0][0] = True
    
    while Q:
        x, y = Q.popleft()
        for d in direction:
            nx, ny = x+d[0], y+d[1]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = True
                Q.append((nx, ny))
    
    answer = dist[n-1][m-1]
    if answer == 0:
        return -1
    return answer