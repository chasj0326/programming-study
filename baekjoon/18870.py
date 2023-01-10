import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

order = sorted(list(set(nums)))
dic = {order[i]: i for i in range(len(order))}
for num in nums:
  print(dic[num], end=' ')
print()
