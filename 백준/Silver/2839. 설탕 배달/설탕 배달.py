S = [int(1e+8)] * 5001
S[3] = 1; S[5] = 1

N = int(input())

if N > 5:
    for n in range(6, N+1):
        S[n] = min(S[n-3]+1, S[n-5]+1)

if S[N] > 1e+7:
    print(-1)
else:
    print(S[N])