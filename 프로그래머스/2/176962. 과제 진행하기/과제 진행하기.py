def solution(plans):
    newPlans = []
    
    for plan in plans: # 분 단위로 바꾸기
        h, m = plan[1].split(':')
        time = int(h) * 60 + int(m)
        newPlans.append([plan[0], time, int(plan[2])])
        
    newPlans.sort(key=lambda x: x[1]) # 시작 시각 순서로 계산
    leftPlan = []
    solvedPlan = []
    
    for i in range(len(newPlans)-1):
        b_name, b_start, b_time = newPlans[i]
        a_name, a_start, a_time = newPlans[i+1]

        leftTime = b_time - (a_start - b_start)

        if leftTime > 0: # 시간 부족한 경우
            leftPlan.append((b_name, leftTime))

        elif leftTime == 0: # 시간 다 채운 경우
            solvedPlan.append(b_name)

        elif leftTime < 0: # 시간 남는 경우
            solvedPlan.append(b_name)
            leftTime = -leftTime

            while leftPlan and leftTime > 0:
                last_name, last_remain = leftPlan.pop()
                if last_remain <= leftTime:
                    solvedPlan.append(last_name)
                    leftTime -= last_remain
                else:
                    leftPlan.append((last_name, last_remain - leftTime))
                    leftTime = 0
                    

    
    # 나머지 처리
    solvedPlan.append(newPlans[-1][0])
    if leftPlan:
        for i in range(len(leftPlan)):
            solvedPlan.append(leftPlan.pop()[0])
    return solvedPlan