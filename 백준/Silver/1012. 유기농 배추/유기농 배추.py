T = int(input())

for _ in range(T):
  M, N, K = map(int, input().split())
  
  cabbage = []
  for _ in range(K):
    x, y = map(int, input().split())
    cabbage.append((x, y))
    
  direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  cnt = 0
  
  while cabbage:
    cx, cy = cabbage.pop()
    stack = [(cx, cy)]
    
    while stack:
      cx, cy = stack.pop()
      for dx, dy in direction:
        nx = cx + dx; ny = cy + dy
        if (nx, ny) in cabbage:
          cabbage.remove((nx, ny))
          stack.append((nx, ny))
          
    cnt += 1

  print(cnt)