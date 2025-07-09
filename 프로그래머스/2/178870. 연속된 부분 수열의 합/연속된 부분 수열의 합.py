def solution(sequence, k):
    
    left, right = 0, 0
    current = sequence[0]
    answers = []
    
    while True:
        
        if current == k:
            answers.append((left, right, right-left))
            
        if current >= k:
            current -= sequence[left]
            left += 1
        else:
            right += 1
            if right == len(sequence):
                break
            current += sequence[right]
            
    answers.sort(key=lambda x: x[0])
    answers.sort(key=lambda x: x[2])
    answer = (answers[0][0], answers[0][1])
    return answer