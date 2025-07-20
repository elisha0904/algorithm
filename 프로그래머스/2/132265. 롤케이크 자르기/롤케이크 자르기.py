def solution(topping):
    answer = 0
    
    len_top = len(topping)
    left, right = [], []
    l_top, r_top = 0, 0
    l_set, r_set = set(), set()
    
    for idx in range(len_top):
        if topping[idx] not in l_set:
            l_top += 1
            l_set.add(topping[idx])
        
        left.append(l_top)
    
    for idx in range(1, len_top+1):
        if topping[-idx] not in r_set:
            r_top += 1
            r_set.add(topping[-idx])
            
        right.append(r_top)
    
    right.reverse()
    for idx in range(len_top-1):
        if left[idx] == right[idx+1]:
            answer += 1
            
    return answer