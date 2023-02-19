n = int(input())
answer = 0

while n % 5 != 0 and n>0:
  n -= 3
  answer += 1

if n<0:
  print(-1)
elif n==0:
  print(answer)
else:
  print(answer+n//5)

