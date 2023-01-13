m, n = map(int, input().split())
nums = [i for i in range(0, n+1)]

end = round(n**(1/2))
for i in range(2, end+1):
  j = 2*i
  while j<=n:
    nums[j] = 0
    j += i

for i in range(m if m>=2 else 2, n+1):
  if nums[i]:
    print(i)