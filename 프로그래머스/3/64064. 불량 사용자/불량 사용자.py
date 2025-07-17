import itertools

def checkID(uid, bid):
    if len(uid) != len(bid):
        return False
    for u, b in zip(uid, bid):
        if b != "*" and u != b:
            return False
    return True

def solution(user_id, banned_id):
    
    banned = {i: [] for i in range(len(banned_id))}
    
    for uid in user_id:
        for i, bid in enumerate(banned_id):
            if checkID(uid, bid) and uid not in banned[i]:
                banned[i].append(uid)
    
    combinations = list(itertools.product(*banned.values()))
    answer = []
    
    for c in combinations:
        if len(set(c)) == len(c) and sorted(c) not in answer:
            answer.append(sorted(c))

    answer = len(answer)
    
    return answer