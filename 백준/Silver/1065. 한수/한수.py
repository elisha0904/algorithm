X = str(input())

def is_seq(n):
    N = list(map(int, list(str(n))))
    diff = N[0] - N[1]
    for n in range(1, len(N)):
        if diff != (N[n-1] - N[n]):
            return False
    return True

if len(X) < 3:
    print(int(X))
else:
    x = 100
    result = 0
    while x <= int(X):
        if is_seq(x):
            result += 1
        x += 1
    print(result + 99)