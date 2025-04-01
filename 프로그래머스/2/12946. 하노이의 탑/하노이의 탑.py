def solution(n, start=1, mid=2, end=3): # start: 출발점, end: 도착점
    if n == 1:
        return [[start, end]]
    
    answer = []
    answer.extend(solution(n-1, start, end, mid)) # 가장 큰 거 빼고 나머지를 mid로
    answer.extend([[start, end]]) # 가장 큰 걸 end로
    answer.extend(solution(n-1, mid, start, end)) # 아까 mid로 옮긴 나머지를 다시 처리
    
    return answer