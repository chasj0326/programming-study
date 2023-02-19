n = int(input())
dp = [0 for i in range(n + 1)]
MAX = 5001

for i in range(n + 1):
  if i == 3:
    dp[i] = 1
  elif i < 5:
    dp[i] = MAX
  elif i % 5 == 0:
    dp[i] = i // 5
  else:
    dp[i] = min(dp[i - 5], dp[i - 3]) + 1

print(-1 if dp[n] >= MAX else dp[n])
