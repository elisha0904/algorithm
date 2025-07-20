def solution(s):

    stack = []
    
    for x in list(s):
        if x == "(":
            stack.append(x)
        if x == ")":
            if not stack:
                return False
            stack.pop()
    
    if stack:
        return False
    else:
        return True