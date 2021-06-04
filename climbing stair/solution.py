class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [0]*(n+1)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:            
            s[0] = 0
            s[1] = 1
            s[2] = 2
            for i in range(3,n+1):
                s[i] = s[i-1] + s[i-2]

        return s[n]