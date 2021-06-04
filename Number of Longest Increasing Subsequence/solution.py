class Solution(object):
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1: return N
        lengths = [1] * N 
        counts = [1] * N 
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] >= lengths[i]:
                        lengths[i] = max(lengths[i],lengths[j]+1)
                        counts[i] = counts[j]
                    elif lengths[i]==lengths[j] + 1:
                        counts[i] += counts[j]
        longest = max(lengths)
        return sum(c for j, c in enumerate(counts) if lengths[j] == longest)