n, m = map(int, input().split())
answer = []
for i in range(n):
  answer.append(list(map(int, input().split())))
for i in range(n):
  answer[i] = list(
    map(lambda a, b: a + b, answer[i], list(map(int,
                                                input().split()))))
for i in range(n):
  print(*answer[i])