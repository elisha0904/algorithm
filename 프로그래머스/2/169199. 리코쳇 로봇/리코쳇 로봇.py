from collections import deque

def solution(board):
    
    for i, b in enumerate(board):
        if "R" in b:
            global start; start = (i, b.index("R"))
        if "G" in b:
            global end; end = (i, b.index("G"))

    cols, rows = len(board[0]), len(board)
    sr, sc = start
    er, ec = end
    
    dist = [[-1 for _ in range(cols)] for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append((sr, sc))
    dist[sr][sc] = 0

    while queue:
        r, c = queue.popleft()
        if (r, c) == (er, ec):
            return dist[r][c]
        
        for dr, dc in directions:
            nr, nc = r, c
            
            while True: # 벽에 닿을 때까지 이동
                nr_, nc_ = nr + dr, nc + dc
                
                if not(0 <= nr_ < rows) or not(0 <= nc_ < cols):
                    break
                if board[nr_][nc_] == 'D':
                    break
                    
                nr, nc = nr_, nc_
            
            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return -1
