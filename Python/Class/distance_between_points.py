import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


point_1 = Point(3, 4)


def distance_between_points(C):
    point_1 = C(3, 4)
    point_2 = C(3, 5)

    d = math.sqrt(pow((point_1.x - point_2.x), 2) + pow((point_1.y - point_2.y), 2))
    print(d)

distance_between_points(Point)
