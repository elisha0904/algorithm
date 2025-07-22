from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    Q = deque()
    Q.append(0)
    visited[0] = True
    
    while Q:
        c = Q.popleft()
        for ni, nc in enumerate(computers[c]):
            if nc == 1 and not visited[ni]:
                visited[ni] = True
                Q.append(ni)
        if len(Q) == 0:
            answer += 1
            if False in visited:
                vid = visited.index(False)
                Q.append(vid)
                visited[vid] = True
        
    return answer