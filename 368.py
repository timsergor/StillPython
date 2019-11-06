# 1185. Day of the Week. Easy. 64.7%.

# Given a date, return the corresponding day of the week for that date.

# The input is given as three integers representing the day, month and year respectively.

# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        back = 5
        for i in range(year - 1971):
            if i % 4 == 1:
                back = (back + 2) % 7
            else:
                back = (back + 1) % 7
        for i in range(month - 1):
            if i in [0,2,4,6,7,9,11]:
                back = (back + 3) % 7
            elif i in [3,5,8,10]:
                back = (back + 2) % 7
            else:
                if (year % 4 == 0 and year != 2100) or year == 2000:
                    back = (back + 1) % 7
        back = (back + (day - 1)) % 7
        return days[back]
