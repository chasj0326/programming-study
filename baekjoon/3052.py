nums = []
for i in range(10):
  nums.append(int(input()) % 42)
print(len(list(set(nums))))