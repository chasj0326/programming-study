import sys
input = sys.stdin.readline

n = int(input())
MIN, MAX = -4000, 4000
nums, freq = [], []
counts = [0 for i in range(MIN, MAX + 1)]

for _ in range(n):
  counts[int(input()) - MIN] += 1
max_cnt = max(counts)

for i in range(0, MAX - MIN + 1):
  if counts[i]:
    nums.extend([i + MIN] * counts[i])
    if counts[i] == max_cnt:
      freq.append(i + MIN)

print(round(sum(nums) / n))
print(nums[n // 2])
print(freq[1] if len(freq) > 1 else freq[0])
print(nums[-1] - nums[0])
