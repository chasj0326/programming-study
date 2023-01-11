def isPrime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  for i in range(n // 2, 1, -1):
    if n % i == 0:
      return False
  return True


n = int(input())
print(len(list(filter(isPrime, list(map(int, input().split()))))))
