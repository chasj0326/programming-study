import sys

MAX = 123456 * 2
isPrime = [True for _ in range(MAX + 1)]
isPrime[1] = False
for i in range(2, round(MAX**(1 / 2)) + 1):
  if isPrime[i]:
    for j in range(i + i, MAX + 1, i):
      isPrime[j] = False

while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break
  print(isPrime[n + 1:2 * n + 1].count(True))