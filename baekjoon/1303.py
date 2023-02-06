n, m = map(int, input().split())
war_map = []
for _ in range(m):
  war_map.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

scores = {'W': 0, 'B': 0}


def war(war_map, start):
  v = []
  stack = [start]
  while stack:
    x, y = stack.pop()
    if (x, y) not in v:
      v.append((x, y))
      for move in range(4):
        i, j = x + dx[move], y + dy[move]
        if i == m or j == n or i < 0 or j < 0 or war_map[x][y] != war_map[i][j]:
          continue
        stack.append((i, j))
  return v


visited = []

for start_x in range(m):
  for start_y in range(n):
    if (start_x, start_y) in visited:
      continue
    result = war(war_map, (start_x, start_y))
    visited += result
    scores[war_map[start_x][start_y]] += len(result)**2

for score in scores.values():
  print(score, end=' ')
print()