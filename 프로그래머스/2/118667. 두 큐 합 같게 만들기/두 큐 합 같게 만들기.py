def solution(queue1, queue2):

    # 전체 한 바퀴 돌기 전에 무조건 답이 나와야 하니까 그냥 queue를 두 배로 늘리기
    queue = queue1 + queue2 + queue1 + queue2
    goal = sum(queue1 + queue2) // 2
    if sum(queue) % 2 != 0: # 합산이 홀수면 어차피 답이 없음
        return -1
    
    left, right = 0, len(queue1)
    section_sum = sum(queue[left:right]) # 시간 초과 방지
    max_len = len(queue)
    answer = 0
    
    for _ in range(max_len):
        
        if section_sum == goal:
            return answer
        
        elif section_sum > goal and right-left+1 < max_len:
            section_sum -= queue[left]
            left += 1
            answer += 1
        
        else:
            section_sum += queue[right]
            right += 1
            answer += 1
    
    return -1