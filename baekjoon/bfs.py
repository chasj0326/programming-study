from collections import deque

graph = {1: [2, 3], 2: [4, 5], 3: [6, 7, 8], 4: [9], 6: [10, 11]}
root = 1


def BFS(graph, root):
  v = []
  queue = deque([root])

  while queue:
    print(queue)
    n = queue.popleft()
    if n not in v:
      v.append(n)
      if n in graph:
        queue.extend((set(graph[n]) - set(v)))
  return v


print(BFS(graph, root))
