class Solution:
    def __init__(self,nums):
        self.nums=nums
    def moveZeroes(self, nums:[int]) -> None:
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(0)
        print(nums)
nums=[0,1,0,3,12]
solution=Solution(nums)
result=solution.moveZeroes(nums)
print(result)