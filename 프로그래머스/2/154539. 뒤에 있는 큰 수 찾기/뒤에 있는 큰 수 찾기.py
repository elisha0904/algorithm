def solution(numbers):
    answer = [-1]
    stack = []
    
    stack.append(numbers.pop())
    
    for n in numbers[::-1]:
        while stack:
            s = stack[-1]
            if n < s:
                answer.append(s)
                stack.append(n)
                break
            else:
                stack.pop()
        if not stack:
            answer.append(-1)
            stack.append(n)
        
    answer.reverse()
    return answer
