x = int(input())
a, b, c = 1, 0, x
while c > a:
  c -= a
  b += a
  a += 1

b = x - b
top = a - b + 1 if a % 2 else b
bottom = b if a % 2 else a - b + 1
print(f'{top}/{bottom}')
