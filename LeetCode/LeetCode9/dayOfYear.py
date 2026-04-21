

# Given a string date representing a Gregorian calendar date formatted
# as YYYY-MM-DD, return the day number of the year.


class Solution:
    def dayOfYear(self, date: str) -> int:
        nums = date.split('-')
        year, month, day = int(nums[0]), int(nums[1]), int(nums[2])
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leapYear = (0 == year % 4 and 0 != year % 100) or 0 == year % 400
        if leapYear:
            monthDays[1] = 29
        days = 0
        for i in range(month - 1):
            days += monthDays[i]

        return days + day



