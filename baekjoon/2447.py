def star(n):
  if n == 1:
    return ['*']
  stars = star(n // 3)
  new = []
  for i in stars:
    new.append(i * 3)
  for i in stars:
    new.append(i + ' ' * (n // 3) + i)
  for i in stars:
    new.append(i * 3)
  return new


for i in star(int(input())):
  print(i)