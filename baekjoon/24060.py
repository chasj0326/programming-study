def sort(arr, start, end, nums):
  if start == end:
    return nums
  mid = (start + end) // 2
  sort(arr, start, mid, nums)
  sort(arr, mid + 1, end, nums)
  
  arr[start:end+1] = merge(arr, start, mid, end)
  for i in arr[start:end+1]:
    nums.append(i)
  return nums


def merge(arr, start, mid, end):
  newList = []
  i, j = start, mid + 1
  while (i <= mid and j <= end):
    if arr[i] <= arr[j]:
      newList.append(arr[i])
      i += 1
    else:
      newList.append(arr[j])
      j += 1
  while (i <= mid):
    newList.append(arr[i])
    i += 1
  while (j <= end):
    newList.append(arr[j])
    j += 1
  return newList


n, k = map(int, input().split())
nums = sort(list(map(int, input().split())),0,n-1,[])
print(nums[k-1] if len(nums)>=k else -1)