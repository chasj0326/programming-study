n = int(input())
nums = list(map(int, input().split()))
m = max(nums)
results = [True for i in range(m + 1)]
results[1] = False

for i in range(2, round(m**1 // 2) + 1):
  if results[i] == True:
    j = 2
    while i * j <= m:
      results[i * j] = False
      j += 1

print(len(list(filter(lambda x: results[x], nums))))
