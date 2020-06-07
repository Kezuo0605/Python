class Date():
    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day
        date1 = str(f' {self.day} - {self.month} - {self.year}')

    @classmethod
    def todaydate(cls, day, month, year):
        date1 = str(f' {day} - {month} - {year}')
        date = day, month, year
        print(type(date1))
        date1 = date1.split("-")
        for i in date1:
            date = int(i)
            print(date)
        return

    @staticmethod
    def security(self, day, month, year):
        try:
            day > 0 and day <= 31 and month == 1 or 3 or 5 or 7 or 8 or 10 or 12
            day > 0 and day <= 30 and month == 4 or 6 or 9 or 11
            day > 0 and day <= 28 and month == 2 and year % 4 != 0
            day > 0 and day <= 29 and month == 2 and year % 4 == 0
            month > 0 and month <= 12
            year > 0 and year <= 2020
        except:
            print("please, only date by format DAY-MONTH-YEAR")




Date.todaydate(12, 14, 10)
Date.security(1, 12, 14, 10)
