def makePrimes(n):
  primes = [1 for i in range(n + 1)]
  primes[0], primes[1] = 0, 0
  for i in range(2, round(n**(1 / 2)) + 1):
    if primes[i]:
      for j in range(i * i, n + 1, i):
        primes[j] = 0
  return primes


cases = []
for _ in range(int(input())):
  cases.append(int(input()))

primes = makePrimes(max(cases))

for n in cases:
  for i in range(n // 2, 1, -1):
    if primes[i] and primes[n - i]:
      print(i, n - i)
      break
