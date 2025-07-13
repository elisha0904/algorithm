def solution(info, edges):
    
    tree = {i: [] for i in range(len(info))}
    for p, c in edges:
        tree[p].append(c)
    
    candidate = tree[0].copy()
    answer = 0
    sheep, wolf = 1, 0
    
    def findSheep(sheep, wolf, candidate):
        
        nonlocal answer
        answer = max(answer, sheep)
        
        for c in candidate:
            
            # 양 / 늑대 수 갱신
            if info[c] == 0:
                newSheep = sheep + 1
                newWolf = wolf
            else:
                newSheep = sheep
                newWolf = wolf + 1
            
            if newWolf >= newSheep:
                continue
            
            newCandidate = candidate.copy()
            newCandidate.remove(c)
            newCandidate.extend(tree[c])
            findSheep(newSheep, newWolf, newCandidate)
    
    findSheep(sheep, wolf, candidate)
    
    return answer