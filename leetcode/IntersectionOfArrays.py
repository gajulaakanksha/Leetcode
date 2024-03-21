class Solution:
    def __init__(self,nums1,nums2):
        self.nums1=nums1
        self.nums2=nums2
    def intersect(self, nums1:[int], nums2:[int]) ->[int]:
        nums3=[]
        i=0
        j=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    nums3.append(nums1[i])
                    nums2.remove(nums2[j])
                    break
        return nums3
nums1=[1,2,2,1]
nums2=[2,2]
solution=Solution(nums1,nums2)
result=solution.intersect(nums1,nums2)
print(result)
        
                                     