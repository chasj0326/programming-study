start, count = int(input()), 0
n = start
while True:
  count += 1
  if n < 10:
    x = 11 * n
  else:
    x = 10 * (n % 10) + (n // 10 + n % 10) % 10
  if x == start:
    break
  else:
    n = x
print(count)
