'''
Day of the Week
<T> Array

int day
int month
int year

- return corresponding day of the week for that date
    - answer in string form as described


bad question, it is only about using date libraries and lots of unnecessary parsing

'''
import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        givenDay = datetime.datetime(year,month,day)
        dayLabels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return dayLabels[givenDay.weekday()]
        