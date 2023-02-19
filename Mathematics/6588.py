import sys

def isPrime(n):
  isPrimes = [True for _ in range(n + 1)]
  isPrimes[1] = False
  for i in range(2, round(n**(1 / 2)) + 1):
    if isPrimes[i]:
      for j in range(i + i, n + 1, i):
        isPrimes[j] = False
  return isPrimes

nums = []
while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break
  nums.append(n)

if nums:
  MAX = max(nums)
isPrimes = isPrime(MAX)

for num in nums:
  for i in range(3, num // 2 + 1, 2):
    if isPrimes[i] and isPrimes[num - i]:
      print(f'{num} = {i} + {num-i}')
      break
