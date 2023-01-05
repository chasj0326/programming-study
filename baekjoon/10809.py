s=input()
start,end=ord('a'),ord('z')
ords = [-1 for i in range(start,end+1)]
for i in s:
  if ords[ord(i)-start]==-1:
    ords[ord(i)-start]=s.index(i)
print(*ords)