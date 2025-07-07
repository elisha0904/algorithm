def solution(diffs, times, limit):
    
    solveTime = []
    
    def getTime(low, high):
        usedTime = 0
        level = (low + high) // 2
        if low > high:
            return
        
        for i, (diff, time) in enumerate(zip(diffs, times)):
            if diff <= level:
                usedTime += time
            else:
                usedTime += (diff - level) * (times[i-1] + time) + time
        
        print(low, high, level, usedTime)
        
        if usedTime > limit:
            return getTime(level+1, high)
        else:
            solveTime.append(level)
            return getTime(low, level-1)
    
    getTime(1, 1e+6)
    answer = min(solveTime)
    return answer