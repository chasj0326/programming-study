n = int(input())
dp = [0 for i in range(n + 1)]


def toOne(n):
  if dp[n] or n == 1:
    return dp[n]
  if n <= 3:
    dp[n] = 1
  else:
    if n % 6 == 0:
      dp[n] = min(toOne(n // 3), toOne(n // 2)) + 1
    elif n % 3 == 0:
      dp[n] = min(toOne(n // 3), toOne(n - 1)) + 1
    elif n % 2 == 0:
      dp[n] = min(toOne(n // 2), toOne(n - 1)) + 1
    else:
      dp[n] = toOne(n - 1) + 1
  return dp[n]


print(toOne(n))
