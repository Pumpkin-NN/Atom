'''
class Time():
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

if __name__ == '__main__':
    t1 = Time()
    t1.hour = 3
    t1.minute = 50
    t1.second = 55
    print('%.2d:%.2d:%.2d' % (t1.hour, t1.minute, t1.second))
    print("\n")
    seconds = t1.time_to_int()
    print(seconds)
'''
'''
class Time():
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (t1.hour, t1.minute, t1.second))

t1 = Time()
t1.print_time()
'''

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{self.x}, {self.y}'
    def add_tuple(self, points):
        x, y = points
        m = self.x + x
        n = self.y + y

        return f'{m}, {n}'
    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return f'{x}, {y}'
        else:
            return self.add_tuple(points)

    def __radd__(self, other):
        return self.__add__(other)


points = (7,8)
p1 = Point(1,2)
p2 = Point(3,4)
print(p1)
# print(p1 + p2)
print(p1 + points)
print(points + p1)


'''
class Time():
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (t1.hour, t1.minute, t1.second))

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

t1 = Time()
t1.hour = 3
t1.minute = 50
t1.second = 55

print(t1)
'''
