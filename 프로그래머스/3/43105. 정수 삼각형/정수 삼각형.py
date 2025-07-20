def solution(triangle):
    answer = 0
    tlen = len(triangle)
    
    for level, t in enumerate(triangle[::-1]):
        if level == 0:
            continue
        
        for i, x in enumerate(t):
            triangle[tlen-level-1][i] = x + max(triangle[tlen-level][i], triangle[tlen-level][i+1],)
            
        
    return triangle[0][0]