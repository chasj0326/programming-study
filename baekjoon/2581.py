def isPrime(n, primes):
  for prime in primes:
    if n % prime == 0:
      return False
  return True


def makePrimes(n):
  if n <= 1:
    return []
  primes = [2]
  for i in range(3, n + 1):
    if isPrime(i, primes):
      primes.append(i)
  return primes


n_primes = makePrimes(int(input()) - 1)
m_primes = makePrimes(int(input()))
p = list(filter(lambda x: x not in n_primes, m_primes))

if len(p):
  print(sum(p), p[0], sep='\n')
else:
  print(-1)

print(n_primes, m_primes, p)
