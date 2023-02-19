a, b, c = map(int, input().split())

# c**n 구하기
def pow(c, n, r):
  if n == 1:
    return c % r
  x = pow(c, n // 2, r)  #x = c**(n//2 or (n-1)//2)
  if n % 2:
    return (c * x * x) % r
  return (x * x) % r

print(pow(a, b, c))
