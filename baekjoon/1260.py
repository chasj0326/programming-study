from collections import deque

n, m, r = map(int, input().split())
graph = {}

for _ in range(m):
  x, y = map(int, input().split())
  if x in graph:
    graph[x].append(y)
  else:
    graph[x] = [y]
  if y in graph:
    graph[y].append(x)
  else:
    graph[y] = [x]


def DFS(graph, n, v=[]):
  v.append(n)
  if n in graph:
    for node in sorted(graph[n]):
      if node not in v:
        DFS(graph, node, v)
  return v


def BFS(graph, root, v=[]):
  queue = deque([root])
  while queue:
    n = queue.popleft()
    if n not in v:
      v.append(n)
      if n in graph:
        queue.extend(sorted(graph[n]))
  return v


print(*DFS(graph, r))
print(*BFS(graph, r))