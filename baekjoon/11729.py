def hanoi(n):
  if n == 1:
    return [(1, 3)]
  hanoied = hanoi(n - 1)
  new = []
  for i in hanoied:
    new.append(tuple(map(lambda x: x if x == 1 else 5 - x, i)))
  new.append((1, 3))
  for i in hanoied:
    new.append(tuple(map(lambda x: x if x == 3 else 3 - x, i)))
  return new


result = hanoi(int(input()))
print(len(result))
for i in result:
  print(i[0], i[1])