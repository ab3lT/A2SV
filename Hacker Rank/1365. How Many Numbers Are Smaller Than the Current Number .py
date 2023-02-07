class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedNum = sorted(nums)
        dic = {}
        result = []

        for i in range(len(sortedNum)):
            if sortedNum[i] not in dic:
                dic[sortedNum[i]] = i
        
        for i in nums:
            result.append(dic[i])
        
        return result