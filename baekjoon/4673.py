not_self = []
def d(n):
 return n+sum(list(map(int,str(n))))
  
for i in range(1,10001):
  not_self.append(d(i))
for i in range(1,10001):
  if i not in not_self:
    print(i)