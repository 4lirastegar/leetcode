def search(nums,target):
  if target in nums:
    return f"Founded at index {nums.index(target)}"
  if target > nums[-1]:
    return f"Not Founded but the index would be {len(nums)}"
  else:
    for i in nums:
      if i > target:
        return f"Not founded but the index would be {nums.index(i)} "
      

nums=[1,2,4,6,8,12]
target=13

print(search(nums,target))