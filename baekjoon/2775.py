for i in range(int(input())):
  k = int(input())
  n = int(input())
  people = [i + 1 for i in range(n)]
  for i in range(k):
    for j in range(1, n):
      people[j] += people[j - 1]
  print(people[n - 1])
