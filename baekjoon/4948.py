def printNums(n):
  nums = [1 for i in range(0, 2*n+1)]
  for i in range(n+1):
    nums[i] = 0
  end = round((2*n)**(1/2))
  for i in range(2, end+1):
    j = 2*i
    while j<=2*n:
      nums[j] = 0
      j += i
  return sum(nums[2:])

while True:
  n = int(input())
  if n == 0:
    break
  print(printNums(n))