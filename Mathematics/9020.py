import sys


def isPrime(n):
  isPrimes = [True for _ in range(n + 1)]
  isPrimes[1] = False
  for i in range(2, round(n**(1 / 2)) + 1):
    if isPrimes[i]:
      for j in range(i + i, n + 1, i):
        isPrimes[j] = False
  return isPrimes


T = int(input())
nums = []
for _ in range(T):
  nums.append(int(sys.stdin.readline()))

isPrimes = isPrime(max(nums))

for num in nums:
  for i in range(num // 2, 1, -1):
    if isPrimes[i] and isPrimes[num - i]:
      print(f'{i} {num-i}')
      break
