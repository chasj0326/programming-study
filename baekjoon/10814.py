mems = []
for _ in range(int(input())):
  age, name = input().split()
  mems.append((int(age), name))
for mem in sorted(mems, key=lambda x: x[0]):
  print(mem[0], mem[1])
