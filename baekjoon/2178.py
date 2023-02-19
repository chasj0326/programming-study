from collections import deque

n, m = map(int, input().split())
maps = []
for _ in range(n):
  maps.append(list(map(int, input())))

move_x = [1, -1, 0, 0]
move_y = [0, 0, 1, -1]
queue = deque([(0, 0)])
v = []

while queue:
  x, y = queue.popleft()
  if (x, y) not in v:
    v.append((x, y))
    for dx, dy in zip(move_x, move_y):
      i, j = x + dx, y + dy
      if i >= n or j >= m or i < 0 or j < 0 or maps[i][j] != 1:
        continue
      maps[i][j] += maps[x][y]
      queue.append((i, j))

print(maps[n - 1][m - 1])
