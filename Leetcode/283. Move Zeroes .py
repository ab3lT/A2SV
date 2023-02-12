class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        for R in range(len(nums)):
            if nums[R]:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
        return nums
    
    # pre_idx =0
    #     for i in range(0, len(nums)):
    #         if nums[i] !=0:
    #             hold = nums[pre_idx]
    #             nums[pre_idx] = nums[i]
    #             nums[i] = hold
    #             pre_idx +=1