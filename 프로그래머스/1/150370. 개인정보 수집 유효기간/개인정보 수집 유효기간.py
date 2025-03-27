def get_date(start:list, month:int):
    start = start.split('.')
    y, m = divmod(month, 12)
    
    start[0] = int(start[0]) + y
    start[1] = int(start[1]) + m
    
    if start[1] > 12:
        start[0] += 1
        start[1] = start[1] - 12
    if start[1] < 10:
        start[1] = '0' + str(start[1])

    start = [str(s) for s in start]
    return int(''.join(start))

def solution(today, terms, privacies):
    today = int(''.join(today.split('.')))
    answer = []
    
    client = {}
    for term in terms:
        name, month = term.split(' ')
        client[name] = int(month)
        
    for idx, privacy in enumerate(privacies):
        start, name = privacy.split(' ')
        end = get_date(start, client[name])

        if end <= today:
            answer.append(idx+1)
    
    return answer