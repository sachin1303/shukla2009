class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x           # using newton rapshn method
        while r*r > x:
            r = (r + x/r) / 2
        return r