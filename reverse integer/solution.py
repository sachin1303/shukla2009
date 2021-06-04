class Solution(object):
    def reverse(self , x):
        a = 0
        b = x if x > 0 else -x
        while b:
            if a > 2 ** 31 / 10:
                return 0
            else:
                a = a * 10 + b % 10
                b= b / 10
        return a if x > 0 else -a
        