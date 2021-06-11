class WeekDayError(Exception):
    pass
	

class Weeker:
    __days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

    def __init__(self, day):
        if day not in self.__days:
            raise WeekDayError
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        tmp = (self.__days.index(self.__day) + 1 + n) % 7
        self.__day = self.__days[tmp - 1]

    def subtract_days(self, n):
        tmp = (self.__days.index(self.__day) + 1 - n) % 7
        self.__day = self.__days[tmp - 1]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
