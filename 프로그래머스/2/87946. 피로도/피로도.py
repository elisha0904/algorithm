def solution(k, dungeons):

    """
    접근 1: 모든 순열 경우의 수를 나열하고, 조건에 충족하는 케이스의 탐험 던전 수를 저장하고 최댓값 반환 = O(8!)
    접근 2: 현재 피로도를 기준으로 탐험 가능 던전에 대해 재귀적으로 탐색해 최댓값 반환
    """
    
    candidate = []
    def go_dungeons(k, dungeons, n):
        flag = False
        for i, dungeon in enumerate(dungeons):
            if k >= dungeon[0]:
                flag = True
                available_dungeons = dungeons.copy()
                available_dungeons.pop(i)
                go_dungeons(k-dungeon[1], available_dungeons, n+1)
        if flag == False:
            candidate.append(n)
            return
    
    go_dungeons(k, dungeons, 0)
    
    return max(candidate)