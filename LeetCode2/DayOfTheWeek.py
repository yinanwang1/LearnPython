class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import time
        sTime = time.strptime(str(year) + "-" + str(month) + "-" + str(day), "%Y-%m-%d")
        weekdays = {0: 'Sunday', 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
        return weekdays[sTime.tm_wday]

import datetime

myDate = datetime.timedelta()