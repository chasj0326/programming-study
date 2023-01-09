import sys

input = sys.stdin.readline

n = int(input())
nums = []
fqc = []
count = [0] * 8001

for _ in range(n):
  count[int(input()) + 4000] += 1
max_count = max(count)

for i in range(8001):
  if count[i]:
    if count[i]==max_count:
      fqc.append(i-4000)
    for j in range(count[i]):
      nums.append(i - 4000)


print(round(sum(nums)/n))
print(nums[n // 2])
print(fqc[1] if len(fqc)>1 else fqc[0])
print(nums[-1] - nums[0])
