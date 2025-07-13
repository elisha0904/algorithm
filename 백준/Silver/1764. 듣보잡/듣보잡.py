import sys

n, m = map(int, sys.stdin.readline().split())
N = set()
answer = []

for _ in range(n):
  N.add(input())

for _ in range(m):
  v = input()
  if v in N:
    answer.append(v)

# def binarySearch(v):
#   left, right = 0, len(answer)

#   while left < right:
#     mid = (left + right) // 2

#     if answer[mid] < v:
#       left = mid + 1
#     else:
#       right = mid

#   return left
  
# for _ in range(m):
#   v = input()
#   if v in N:
#     idx = binarySearch(v)
#     answer.insert(idx, v)

answer.sort()
print(len(answer))
for a in answer:
  print(a)