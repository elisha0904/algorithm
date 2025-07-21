def solution(numbers, target):
    
    idx = 0
    now = 0
    candidate = []
    
    def DFS(idx, now):
        if idx == len(numbers):
            candidate.append(now)
            return
        DFS(idx+1, now+numbers[idx])
        DFS(idx+1, now-numbers[idx])

    
    DFS(idx, now)
    answer = candidate.count(target)
    return answer