locs = []
for _ in range(int(input())):
  locs.append(tuple(map(int, input().split())))
for loc in sorted(locs, key=lambda x: (x[1], x[0])):
  print(loc[0], loc[1])