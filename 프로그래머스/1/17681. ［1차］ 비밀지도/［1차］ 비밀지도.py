def solution(n, arr1, arr2):
    arr1 = [format(a, f'0{n}b') for a in arr1]
    arr2 = [format(a, f'0{n}b') for a in arr2]
    answer = []
    
    print(arr1)
    
    for i in range(n):
        a = ''
        for j in range(n):        
            if arr1[i][j] == "1" or arr2[i][j] == "1":
                a += "#"
            else:
                a += " "
        answer.append(a)
    
    return answer