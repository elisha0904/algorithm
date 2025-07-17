def solution(players, m, k):
    
    server = [] # 서버 저장
    now_s = 0
    answer = 0
    
    for t, player in enumerate(players):
        if player // m - now_s > 0:
            s = player // m - now_s # 증설 서버 개수
            now_s += s
            answer += s
            
            server.append((s, t))
        if server and server[0][1] + k - 1 == t:
            s = server.pop(0)
            now_s -= s[0]
    
    return answer