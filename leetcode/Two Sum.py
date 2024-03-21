class Solution:
    def __init__(self,nums,target):
        self.nums=nums
        self.target=target
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    return [i,j]
                    break
nums=[2,7,11,15]
target=9
solution=Solution(nums,target)
result=solution.twoSum(nums,target)
print(result)
                
        
                
        

                
        
