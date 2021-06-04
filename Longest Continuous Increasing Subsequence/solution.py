class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        S = 1
        P = 1
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                S += 1
                P = max(P, S)
            else:
                S = 1
        return P
