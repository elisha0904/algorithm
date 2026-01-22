def solution(relation):
    """
    유일성 검사 + 최소성 검사 분리
    """
    
    from itertools import combinations
    
    def is_unique(set_list):
        if len(set(set_list)) == len(set_list):
            return True
        return False

    candidates = []
    def is_minimal(c, candidates):
        for candidate in candidates:
            if set(candidate).issubset(set(c)):
                return False
        return True
                
    column = len(relation[0])
    features = {i: [] for i in range(column)}
    combination_set = []
    
    for i in range(1, column+1):
        for c in combinations(range(column), i):
            combination_set.append(c)
            
    for c in combination_set:
        example = [tuple(row[i] for i in c) for row in relation]
        if is_unique(example) and is_minimal(c, candidates):
            candidates.append(c)
    
    return len(candidates)
            
    
    

