# Create a class Time with private attributes hour,minute and second.Overload '+' operator to find sum of 2 time.

class Time:
    def __init__(self, h, m, s):
        self.__h = h
        self.__m = m
        self.__s = s

    def __add__(self, other):
        sec = self.__s + other.__s
        minute = self.__m + other.__m
        hour = self.__h + other.__h

        if sec >= 60:
            sec -= 60
            minute += 1

        if minute >= 60:
            minute -= 60
            hour += 1

        return Time(hour, minute, sec)

    def display(self):
        print(f"{self.__h} : {self.__m} : {self.__s}")
