from collections import deque

def checkWord(A, B):
    cnt = 0
    for a, b in zip(A, B):
        if a != b:
            cnt += 1
        if cnt > 1:
            return False
    return True

def solution(begin, target, words):
    answer = 1e+3
    used = set()
    Q = deque()
    Q.append((begin, 0))
    
    if target not in words:
        return 0
    
    while Q:
        w, cnt = Q.popleft()
        if w == target:
            if answer > cnt:
                answer = cnt
        for word in words:
            if word in used:
                continue
            if checkWord(w, word):
                Q.append((word, cnt+1))
                used.add(word)
    
    return answer