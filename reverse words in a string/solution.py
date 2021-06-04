class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""    
        word = ""  
        for ch in s:
            if (ch!=' '):
                word+=ch
            if (ch==' '):
                if (len(word)!=0):
                    if (res!=""):  
                        res = ' ' + res
                    res = word + res
                    word = ""
               
        if (len(word)!=0):
            if (res!=""):
                res = ' ' + res
            res = word + res
            
        return res
        