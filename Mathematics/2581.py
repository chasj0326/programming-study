m = int(input())
n = int(input())
nums = [True for i in range(n + 1)]
nums[1] = False

for i in range(2, round(n**1 / 2) + 1):
  if nums[i]:
    j = 2
    while i * j <= n:
      nums[i * j] = False
      j += 1

results = []
for i in range(m, n + 1):
  if nums[i]:
    results.append(i)

if results == []:
  print(-1)
else:
  print(sum(results))
  print(results[0])
