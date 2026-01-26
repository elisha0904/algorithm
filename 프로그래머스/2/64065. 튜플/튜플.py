def solution(s):
    """
    집합 원소 개수가 작은 것부터 검사해서
    이전 턴에 없었던 요소를 순차적으로 추가하는 방식으로 튜플 완성하면 될 듯
    """
    answer = []
    processed_list = []
    
    s_list = s[1:-1].split('},{')
    for i in s_list:
        if '{' in i:
            i = i[1:]
        if '}' in i:
            i = i[:-1]
        processed_list.append(i.split(','))
    processed_list = sorted(processed_list, key=len)

    for items in processed_list:
        for item in items:
            item = int(item)
            if item not in answer:
                answer.append(item)
    
    return answer