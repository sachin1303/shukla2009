class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        date = date.split('-')
        year = date[0]
        def isLeapYear(year):
            return (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0
        month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
        if isLeapYear(int(year)):
            month_list[1] += 1
        month = int(date[1])
        return sum(month_list[:month-1]) + int(date[2])