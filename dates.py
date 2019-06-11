#!/usr/bin/python3

# day of week calculator using Doomsday algorithm 
# https://en.wikipedia.org/wiki/Doomsday_rule

# days in a month in a common year 
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# weekday codes: indices are the codes
weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# month codes: indices are month #, values are the codes
months = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
# names of the months in order
mnames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class GregorianDate: 
    def __init__(self, month: int, day: int, year: int): 
        self.month = month
        self.day = day
        self.year = year

    def to_str(self) -> str: 
        return mnames[self.month-1] + ' ' + str(self.day) + ',' + str(self.year)

    def get_header(self) -> str: 
        return mnames[self.month-1] + ' ' + str(self.year)

    def is_leap_year(self) -> bool: 
        year_in_cent = self.year % 100
        if year_in_cent == 0 and self.year % 400 != 0: 
            return False
        if year_in_cent % 4 == 0: 
            return True
        return False

    def get_max_days(self) -> int: 
        if self.month == 2 and self.is_leap_year(): 
            return 29
        else: 
            return days[self.month-1]

    def validate(self) -> bool: 
        if not 1 <= self.month <= 12: 
            return False
        if not 1 <= self.day <= self.get_max_days(): 
            return False
        if self.year < 0: 
            return False
        return True

    def get_year_code(self) -> int: 
        cent = self.year // 100
        year_in_cent = self.year % 100
        code = year_in_cent + year_in_cent // 4
        if cent % 4 != 0: 
            code += 7 - cent % 4 * 2
        return code % 7

    def get_weekday_code(self) -> int: 
        return (months[self.month-1] + self.day + self.get_year_code())

    def get_weekday_str(self) -> str: 
        if not self.validate(): 
            return 'Invalid'
        code = self.get_weekday_code() % 7
        return weekdays[code]
