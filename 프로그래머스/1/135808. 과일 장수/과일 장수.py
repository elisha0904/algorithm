def solution(k, m, score):
    
    """
    k : 사과의 최대 점수
    m : 한 상자에 들어가는 사과의 수
    score : 사과들의 점수
    """
    
    cnt = len(score) // m
    score.sort(reverse=True)
    box = []
    answer = 0
    
    for n in range(cnt):
        box.append(score[n*m:(n+1)*m])
        answer += min(score[n*m:(n+1)*m]) * m
    
    
    return answer