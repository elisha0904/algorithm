def solution(schedules, timelogs, startday):
    answer = 0

    saturday = 6 - startday if startday != 7 else 6
    sunday = saturday + 1 if startday != 7 else 0
    
    for schedule, timelog in zip(schedules, timelogs):
        present = 0
        present_time = schedule + 10
        if present_time % 100 > 59:
            present_time = present_time + 100 - 60
            
        for day, time in enumerate(timelog):
            if (day % 7 == saturday) or (day % 7 == sunday):
                continue
            if time <= present_time:
                present += 1
        
        if present == 5:
            answer += 1
    
    return answer