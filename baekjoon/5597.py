nums = [i for i in range(1, 31)]
for i in range(28):
  nums.remove(int(input()))
print(min(nums), max(nums), sep='\n')