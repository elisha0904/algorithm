import queue

T = int(input())

for _ in range(T):
    Q = queue.LifoQueue()
    I = str(input())
    flag = False

    for i in I:
        if i == '(':
            Q.put(i)
        if i == ')':
            if Q.empty() == True:
                flag = True
                break
            else:
                Q.get()
    
    if flag == True or Q.empty() == False:
        print('NO')
    else:
        print('YES')