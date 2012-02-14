"""
    Author: James Meldrum
    Date: Feb 12, 2010
    Lang: Python 2.7
    Desc: Implementation of Greg calendar 

"""

class Date:
    
        # Asert [ assert EXPRESSION [',' EXPRESSION ] ] will raise an error
        # if the first expression is wrong. If another expression is given
        # it will executed that expression in raising the error.
    def __init__(self,month,day,year):
        self._julianDay = 0
        assert self.isValidGregorian(month,day,year),"Invalid Gregorian Date."                       
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + \
        (1461 * (year + 4800 + tmp) // 4 ) + \
        (367 * (month - 2 - tmp *12) // 12) - \
        (3 * ((year + 4900 + tmp) // 100) // 4)
    
    def isValidGregorian(self,month,day,year):
        return_code = True
        
        if month == None or day == None or year == None:
            return_code = False
        
        if month > 12 or day > 31:
            return_code = False
            
        if month < 0 or day < 0:
            return_code = False
        
        return return_code
    
    def month(self):
        return (self._toGregorian())[0]
    
    def day (self):
        return (self._toGregorian())[1]
    
    def year (self):
        return (self._toGregorian())[2]
    
    def dayOfWeek(self):
        month,day,year = self._toGregorian()
        if month < 3:
            month = month +12
            year = year -1
        return ((13 * month + 3) // 5 + day + year + year //4 - year // 100 + year // 400) % 7
    
    def __str__(self):
        month, day, year = self._toGregorian()
        return "%02d/%02d/%04d" % (month,day,year) 
    
    def __eq__ (self,otherDate):
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay
    
    def __le__(self,otherDate):
        return self._julianDay <= otherDate._julianDay
    
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) //4
        year = 4000 * (A+1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80*A // 2447
        day = A - (2447 * month //80)
        A = month //11
        month = month + 2 - (12*A)
        year = 100 * (B-49) + year + A
        return month,day,year