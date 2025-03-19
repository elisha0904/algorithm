def solution(record):
    
    users = {}
    new_record = []
    answer = []
    
    for rec in record:
        info = rec.split()
        if info[0] == 'Enter':
            users[info[1]] = info[2]
            new_record.append(f'{info[1]}님이 들어왔습니다.')
        if info[0] == 'Leave':
            new_record.append(f'{info[1]}님이 나갔습니다.')
        if info[0] == 'Change':
            users[info[1]] = info[2]
            
    for new_rec in new_record:
        id, etc = new_rec.split('님')
        answer.append(users[id]+'님'+etc)
        
    
    return answer