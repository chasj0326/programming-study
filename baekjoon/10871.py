n, x = map(int, input().split())
nums = list(map(int, input().split()))
print(*list(filter(lambda num: num < x, nums)))