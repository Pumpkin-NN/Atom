import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance_between_points(C):
    point_1 = C(3, 4)
    point_2 = C(3, 5)

    d = math.sqrt(pow((point_1.x - point_2.x), 2) + pow((point_1.y - point_2.y), 2))
    print(d)

class Circle():
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def info(self):
        print(self.center.x)
        print(self.center.y)
        print(self.radius)
if __name__ == '__main__':
    distance_between_points(Point)
    point_1 = Point(5, 5)
    c1 = Circle(point_1, 3)
    c1.radius = 6
    c1.info()
