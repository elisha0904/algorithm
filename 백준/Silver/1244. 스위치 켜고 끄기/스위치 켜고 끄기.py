def switch(s):
    if s == 0:
        return 1
    if s == 1:
        return 0
    
def girl(x):
    global S

    left = x-1; right = x+1
    S[x] = switch(S[x]) # 자기자신은 언제나 대칭?

    while left >= 1 and right <= N:
        if S[left] == S[right]:
            flag = True
            S[left] = switch(S[left])
            S[right] = switch(S[right])
            left -= 1
            right += 1
        else:
            break

def boy(x):
    global S
    n = N // x
    for i in range(1, n+1):
        idx = x * i
        S[idx] = switch(S[idx])


N = int(input())
S = list(map(int, input().split()))
S = [None] + S
T = int(input())
TL = [list(map(int, input().split())) for _ in range(T)]

for t, s in TL:
    if t == 1: boy(s)
    if t == 2: girl(s)

for i in range(1, N+1):
    print(S[i], end=' ')
    if i % 20 == 0 :
        print()