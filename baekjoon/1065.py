def han(num):
  if num//100==0:
    return True
  num = list(map(int, str(num)))
  a,d = num[0],num[1]-num[0]
  for i in range(2,len(num)):
    if d!=num[i]-num[i-1]:
      return False
    d = num[i]-num[i-1]
  return True

n= int(input())
for i in range(1,n+1):
  if not han(i):
    n-=1
print(n)