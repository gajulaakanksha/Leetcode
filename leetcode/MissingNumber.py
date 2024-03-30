class Solution:
    def __init__(self,nums):
        self.nums=nums
    def missingNumber(self, nums: [int]) -> int:
        n=len(nums)
        j=0
        for i in nums:
            j=j+i
        sum=j
        return (n)*(n+1)//2-sum
nums=[3,0,1]
solution=Solution(nums)
result=solution.missingNumber(nums)
print(result)
