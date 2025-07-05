def solution(s, skip, index):
    alpha = [chr(x) for x in range(97, 123) if chr(x) not in list(skip)]
    answer = ''
    
    for x in s:
        idx = (alpha.index(x) + index) % len(alpha)
        answer += alpha[idx]
    
    return answer