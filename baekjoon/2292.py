n = int(input())
ans = 1
while True:
  if n == 1 or (2 + 3 * (ans - 1) * (ans - 2) <= n and n <= 1 + 3 * ans *
                (ans - 1)):
    print(ans)
    break
  ans += 1
