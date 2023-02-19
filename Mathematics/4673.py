MAX = 10000
nums = [True for i in range(MAX + 1)]

def makeNext(n):
  return n + sum(list(map(int, str(n))))

for i in range(1, MAX + 1):
  next = makeNext(i)
  if next <= MAX:
    nums[next] = False

for i in range(1, MAX + 1):
  if nums[i]:
    print(i)
