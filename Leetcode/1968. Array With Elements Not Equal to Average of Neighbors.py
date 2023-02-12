class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        array=[]
        i=0
        j=len(nums)-1
        while len(array)!=len(nums):
            array.append(nums[i])
            i+=1
            if j>i:
                array.append(nums[j])
                j-=1
        return array