
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            
           



nums=[2,2,4,8]
target =6

print(twoSum(nums, target))



# Executable with default test case of leetcode


# class Solution(object):
#   def twoSum(self, nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []