locs = []
for _ in range(int(input())):
  locs.append(tuple(map(int, input().split())))

for loc in sorted(locs, key=lambda x: (x[0], x[1])):
  print(loc[0], loc[1])