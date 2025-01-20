N = int(input())
NL = list(map(int, input().split()))
M = int(input())
ML = list(map(int, input().split()))

ND = {}

for n in NL:
    if n in ND:
        ND[n] += 1
    else:
        ND[n] = 1

for m in ML:
    if m in ND:
        print(ND[m], end=' ')
    else:
        print(0, end=' ')