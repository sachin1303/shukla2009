class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {}
        dict['2'] = ['a','b','c']
        dict['3'] = ['d','e','f']
        dict['4'] = ['g','h','i']
        dict['5'] = ['j','k','l']
        dict['6'] = ['m','n','o']
        dict['7'] = ['p','q','r','s']
        dict['8'] = ['t','u','v']
        dict['9'] = ['w','x','y','z']
        
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return dict[digits[0]]
        
        solution = []       
        for par_solution in self.letterCombinations(digits[1:]):
            for s in dict[digits[0]]:
                solution += [s+par_solution]
                
        return solution