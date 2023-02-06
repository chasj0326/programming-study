graph = {1: [2, 3], 2: [4, 5], 3: [6, 7, 8], 4: [9], 6: [10, 11]}
root = 1


def DFS_stack(graph, root):
  v = []
  stack = [root]

  while stack:
    n = stack.pop()
    if n not in v:
      v.append(n)
      if n in graph:
        stack.extend((set(graph[n]) - set(v)))
  return v


def DFS_recursive(graph, n, v=[]):
  v.append(n)
  if n in graph:
    for node in graph[n]:
      if node not in v:
        DFS_recursive(graph, node, v)
  return v


print(DFS_stack(graph, root))
print(DFS_recursive(graph, root))
