def solution(land):
    
    rows, cols = len(land), len(land[0])
    visited = [[False] * cols for _ in range(rows)]
    oil_columns = [0] * cols
    
    def DFS(r, c):
        
        stack = [(r, c)]
        oil = 0
        columns = set()
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
                
            visited[x][y] = True
            oil += 1
            columns.add(y)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < rows and 0 <= ny < cols
                   and not visited[nx][ny]
                   and land[nx][ny] == 1):
                    stack.append((nx, ny))
            
        return oil, columns
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and land[i][j] == 1:
                oil_size, columns = DFS(i, j)
                for col in columns:
                    oil_columns[col] += oil_size
    
    
    return max(oil_columns)