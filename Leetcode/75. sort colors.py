class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
     
        l=0 ; m= 0 ; h=len(nums)-1;
        for i in range(len(nums)):
            if nums[m]==0:
            # Swap low and mid 
                nums[m]= nums[l];
                nums[l]=0;
                m+=1 ; l+=1;
            elif nums[m]==2:
            # Swap high and mid 
                nums[m] = nums[h];
                nums[h]= 2;
                h-=1;
            else:
                m+=1;
        return ;
        