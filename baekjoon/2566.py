nums = []
v, x, y = 0, 0, 0
for i in range(9):
  nums.append(list(map(int, input().split())))
  if max(nums[i]) >= v:
    v = max(nums[i])
    x = i + 1
    y = nums[i].index(max(nums[i])) + 1
print(v)
print(x, y)