class Timer:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        
        return str(format(self.__hours, '02d')) + ":" + str(format(self.__minutes, '02d')) + ":" + str(format(self.__seconds, '02d'))

    def next_second(self):
        self.__seconds += 1
        if self.__seconds >= 60:
            self.__minutes += self.__seconds // 60
            self.__seconds = self.__seconds % 60
        if self.__minutes >= 60:
            self.__hours += self.__minutes // 60
            self.__minutes = self.__minutes % 60
        if self.__hours >= 24:
            self.__hours = self.__minutes % 24

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds <= 0:
            self.__minutes += self.__seconds // 60
            self.__seconds = self.__seconds % 60
        if self.__minutes <= 0:
            self.__hours += self.__minutes // 60
            self.__minutes = self.__minutes % 60
        if self.__hours <= 0:
            self.__hours = self.__hours % 24


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
