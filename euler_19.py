#! /usr/bin/env pypy

monthlengths = { 1: 31,
                 2: 28,
                 3: 31,
                 4: 30,
                 5: 31,
                 6: 30,
                 7: 31,
                 8: 31,
                 9: 30,
                 10: 31,
                 11: 30,
                 12: 31 }

class Day:
    def __init__(self):
        self.day = 1
        self.monthday = 1
        self.month = 1
        self.year = 1900

    def nextday(self):
        self.monthday += 1
        if self.month_finished():
            self.month += 1
            if self.month == 13:
                self.month = 1
                self.year += 1
            self.monthday = 1
        
        self.day += 1
        if self.day > 7:
            self.day = 1

    def __str__(self):
        return ("%d of the week (%4d/%02d/%02d)" %
                (self.day, self.year, self.month, self.monthday))

    def month_finished(self):
        days_in_month = monthlengths[self.month]
        if self.is_leap_year() and self.month == 2:
            days_in_month = 29
        return self.monthday > days_in_month

    def is_leap_year(self):
        # Leap year is on years divisible by four, except centuries,
        # but including those centuries which are divisible by four hundred.
        return self.year % 4 == 0 and not (
               self.year % 100 == 0 and not (
               self.year % 400 == 0))
            
d = Day()
while d.year < 1901:
    print(str(d))
    d.nextday()

print('start counting on %s' % str(d))
c = 0
while d.year < 2001:
    if d.day == 7 and d.monthday == 1:
        print('found occurrence on %s' % str(d))
        c+=1
    d.nextday()
print(c)
