def solution(video_len, pos, op_start, op_end, commands):
    
    def to_int(time):
        return int(''.join(time.split(':')))
    
    video_len = to_int(video_len)
    pos = to_int(pos)
    op_start = to_int(op_start)
    op_end = to_int(op_end)
    
    def time_(time):
        if time < 0:
            return 0
        if time % 100 > 59:
            time = time + 100 - 60
        return time
    
    def opening_(pos):
        if pos >= op_start and pos <= op_end:
            return op_end
        return pos
    
    def prev_(pos):
        if pos % 100 < 10:
            return pos - 50
        if time_(pos - 10) < 0:
            return 0
        return time_(pos - 10)
    
    def next_(pos):
        if time_(pos + 10) > video_len:
            return video_len
        return time_(pos + 10)
    
    pos = time_(opening_(pos))

    for command in commands:
        if command == 'prev':
            pos = prev_(pos)
        if command == 'next':
            pos = next_(pos)
        pos = time_(opening_(time_(pos)))
        print(pos)
    
    answer = ''
    
    if len(str(pos)) == 1:
        answer = '00:0' + str(pos)
    elif len(str(pos)) == 2:
        answer = '00:' + str(pos)
    elif len(str(pos)) == 3:
        answer = '0' + str(pos)[0] + ':' + str(pos)[1:]
    else:
        answer = str(pos)[:2] + ':' + str(pos)[2:]
        
    return answer