# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# def removeElement(nums, val):
#   k=0
#   nums2=[]
#   for i in nums:
#     if i == val:
#       print(val)
#       k+=1
#     else:
#       print(i)
#       nums2.append(i)
#   nums=nums2
#   print(nums)
#   return k,nums


# def removeElement(nums, val):
#         k=0
#         nums3=nums
#         nums=[]
#         for i in nums3:
#             print(i)
#             if i == val:
#                 k+=1
#             else:
#                 nums.append(i)
#                 print(nums)
#         return k

def removeElement(nums,val):
  a=0
  na=0
  while a<len(nums):
    if nums[a]!=val:
      nums[na]=nums[a]
      a+=1
      na+=1
      print(nums, "s")
    else:
      a+=1
      print(nums)
  return na


nums=[0,1,2,2,3,0,4,2]
val=2
print(removeElement(nums,val))