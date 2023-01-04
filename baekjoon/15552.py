import sys

n = int(sys.stdin.readline())
for i in range(n):
  print(sum(list(map(int, sys.stdin.readline().split()))))
