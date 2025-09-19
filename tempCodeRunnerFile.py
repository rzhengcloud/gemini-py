
# from typing import List
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         m = defaultdict(int)
#         m[0] = 1
#         n = len(nums)
#         count, total = 0, 0
#         prefix_sum = [nums[0]] * n
#         # for i, num in enumerate(nums):
#         #     prefix_sum[]
#         for i in range(1,n):
#             prefix_sum[i] = prefix_sum[i-1] + nums[i]
#         print(prefix_sum)
#         for i, num in enumerate(nums):
#             total+=num
#             prev_sum = prefix_sum[i] - total
#             if prev_sum in m:   
#                 count+=m[prev_sum]
#             m[prefix_sum[i]]+=1
#         return count
    
# nums = [1,1,1,1]
# q = Solution()
# q.subarraySum(nums,3)

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         ans=[]
#         for num in nums:
#             index = num - 1 #use num as index
#             if nums[index] < 0: #negative, so seen before
#                 ans.append(num) #flip neg to pos
#             else:
#                 #mark as seen
#                 nums[index] = -nums[index]
#         return ans