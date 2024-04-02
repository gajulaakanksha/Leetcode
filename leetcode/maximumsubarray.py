class Solution:
    def __init__(self,nums):
        self.nums=nums
    def maxSubArray(self, nums:[int]) -> int:
        maxSum=float('-inf')
        currentSum=0
        for num in nums:
            currentSum=currentSum+num
            if currentSum>maxSum:
                maxSum=currentSum
            if currentSum<0:
                currentSum=0
        return maxSum
nums=[-2,1,-3,4,-1,2,1,-5,4]
solution=Solution(nums)
result=solution.maxSubArray(nums)
print(result)
        