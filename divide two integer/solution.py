class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        a=abs(dividend)
        b=abs(divisor)
        if a<b:
            return 0 
        count=0 
        res=0
        sum=0
        while a>=b:
            sum=b
            count=1
            while sum+sum<=a:
                sum+=sum
                count+=count 
            a-=sum
            res+=count 
        if (dividend > 0 and divisor < 0 ) or (dividend < 0 and divisor > 0):
            res=0-res
        if res>2**31-1:
            return 2**31-1 
        elif res<-2**31:
            return -2**31 
        else:
            return res
