def solution(bandage, health, attacks):
    t, x, y = bandage
    
    cont = 0
    last = attacks[-1][0]
    hp = health
    
    for i in range(1, last+1):
        if attacks[0][0] == i: # 몬스터 공격 타이밍
            hp -= attacks[0][1]
            cont = 0
            del attacks[0]
            if hp <= 0:
                return -1
        else:
            hp += x
            cont += 1
            if cont >= t: # t 시간만큼 수행하면
                hp += y
                cont = 0
            if hp > health:
                hp = health
        
    return hp