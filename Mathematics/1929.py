import math

m, n = map(int, input().split())
nums = [True for i in range(n + 1)]
nums[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
  if nums[i]:
    j = 2
    while i * j <= n:
      nums[i * j] = False
      j += 1

for i in range(m, n + 1):
  if nums[i]:
    print(i)
