def solution(park, routes): # 20:33
    
    dog = [0, 0]
    block = []
    
    for x in range(len(park)):
        for y in range(len(park[0])):
            if park[x][y] == 'S':
                dog = [x, y]
            if park[x][y] == 'X':
                block.append((x, y))

    print(dog)
                
    for route in routes:
        way, distance = route.split()
        distance = int(distance)
        
        if way == 'N': now = [dog[0] - distance, dog[1]]
        if way == 'S': now = [dog[0] + distance, dog[1]]
        if way == 'W': now = [dog[0], dog[1] - distance]
        if way == 'E': now = [dog[0], dog[1] + distance]
        
        print(now)
        
        # 공원을 벗어나는지
        if now[0] < 0 or now[0] > len(park)-1 or now[1] < 0 or now[1] > len(park[0])-1:
            print(f'{route}: 공원에서 벗어남')
            continue

        # 장애물을 지나는지
        blocked = False
        for i in range(min(dog[0], now[0]), max(dog[0], now[0])+1):
            for j in range(min(dog[1], now[1]), max(dog[1], now[1])+1):
                if (i, j) in block:
                    blocked = True
                    break
        
        if not blocked:
            dog = now
        
    return dog