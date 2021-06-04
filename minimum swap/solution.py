class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        v = len(s)                    #length=v
        if v < 2:
            return num

        for i in range(v - 1):
            max_dict = i
            for j in range(i + 1, v):
                if s[j] >= s[max_dict] and s[i] != s[j]:
                    max_dict = j
            if max_dict != i:
                temp = s[i]
                s[i] = s[max_dict]
                s[max_dict] = temp
                break 

        return int(''.join(s))
