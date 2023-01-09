paper = [[0 for i in range(100)] for j in range(100)]
for i in range(int(input())):
  a, b = map(int, input().split())
  for x in range(a, a + 10):
    for y in range(b, b + 10):
      paper[x][y] = 1
ans = 0
for i in range(100):
  for j in range(100):
    ans += paper[i][j]
print(ans)
