n = int(input())

for i in range(n):
  ans = list(map(lambda x: 1 if x == 'O' else 0, input()))
  cnt = 0
  for i in range(len(ans)):
    if ans[i]:
      ans[i] += cnt
      cnt += 1
    else:
      cnt = 0
  print(sum(ans))