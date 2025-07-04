import math

def solution(n, w, num):
    # 홀수는 왼쪽, 짝수는 오른쪽
    
    boxes = []
    n_list = [i for i in range(1, n+1)]
    
    h = math.ceil(n / w)
    y = (num -1) // w
    
    if y % 2 == 0:
        x = (num -1) % w
    else:
        x = w - 1 - ((num -1) % w)
    
    if n % w != 0:
        top_line = [0 for _ in range(w)]
        for idx, b in enumerate(n_list[(n//w)*w:]):
            top_line[idx] = b
        if h % 2 == 0:
            top_line.sort(reverse=False)

        answer = h - y - 1
        print(h, x, y, top_line)
        if top_line[x] == 0:
            return answer
        else:
            return answer + 1
    else:
        answer = h - y
        return answer
            