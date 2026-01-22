def solution(dirs):
    
    history = set()
    answer = 0
    
    def is_available(now, dir):
        n_x, n_y = dir
        o_x, o_y = now
        if o_x + n_x < -5 or o_x + n_x > 5:
            return False
        if o_y + n_y < -5 or o_y + n_y > 5:
            return False
        return True
    
    now = [0, 0]
    for dir in dirs:
        temp = now.copy()
        if dir == "U" and is_available(now, (0, 1)):
            now[1] += 1
        if dir == "D" and is_available(now, (0, -1)):
            now[1] -= 1
        if dir == "R" and is_available(now, (1, 0)):
            now[0] += 1
        if dir == "L" and is_available(now, (-1, 0)):
            now[0] -= 1
        if temp != now:
            temp_to_now = sorted([tuple(temp), tuple(now)], key=lambda x: (x[0], x[1]))
            history.add(tuple(temp_to_now))
    
    return len(history)