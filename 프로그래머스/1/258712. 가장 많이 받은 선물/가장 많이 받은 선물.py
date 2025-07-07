def solution(friends, gifts):
    
    present = {}
    
    for f in friends:
        present[f] = {friend: 0 for friend in friends}
    
    # 주면 +1 받으면 -1 / 누적값은 본인 이름에
    for gift in gifts:
        A, B = gift.split()
        present[A][B] += 1
        present[A][A] += 1
        present[B][A] -= 1
        present[B][B] -= 1
    
    countPresent = []
    for f in friends:
        cnt = 0
        for k, v in present[f].items():
            if k == f:
                continue
            if v > 0:
                cnt += 1
            elif v == 0:
                if present[f][f] > present[k][k]:
                    cnt += 1
        countPresent.append(cnt)

    answer = max(countPresent)
    return answer