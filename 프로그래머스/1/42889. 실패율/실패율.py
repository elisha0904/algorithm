def solution(N, stages):
    
    s_cnt = {n:0 for n in range(1, N+1)}
    all_clear = 0
    
    for s in stages:
        all_clear += 1
        if s == N+1:
            continue
        s_cnt[s] += 1
    
    result = []
    for k, v in s_cnt.items():
        if all_clear == 0:
            result.append((k, 0))
        else:
            temp = v / all_clear
            result.append((k, temp))
            all_clear -= v
        
    result.sort(key=lambda x: x[1], reverse=True)
    
    return [k for (k, v) in result]