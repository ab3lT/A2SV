class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #pairs = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j]:
        #             pairs += 1
        #         if nums[i] < nums[j]:
        #             pairs += 1
        # return pairs
        counter = 0
        dic = {}
        for i in nums:
            if i in dic:
                counter += dic[i]
                dic[i] += 1
            else:
                dic[i] = 1
        return counter