import sys

N, M, V = map(int, sys.stdin.readline().split())
graph = {n: [] for n in range(1, N+1)}
visitedBFS = [False for _ in range(N+1)]
visitedDFS = [False for _ in range(N+1)]

for _ in range(M):
  i, j = map(int, input().split())
  graph[i].append(j)
  graph[j].append(i)

def DFS(v):
  
  if visitedDFS[v]:
    return
  
  visitedDFS[v] = True
  print(v, end=' ')

  graph[v].sort()
  for n in graph[v]:
    DFS(n)

def BFS(v):
  stack = [v]

  while stack:
    v = stack.pop(0)
    if visitedBFS[v]:
      continue

    visitedBFS[v] = True
    print(v, end=' ')

    graph[v].sort()
    stack.extend(graph[v])

DFS(V)
print()
BFS(V)