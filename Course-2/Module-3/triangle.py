import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.__x, self.__y - point.__y)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__triangle_list = [vertice1, vertice2, vertice3]

    def perimeter(self):
        return self.__triangle_list[0].distance_from_point(self.__triangle_list[1]) + self.__triangle_list[1].distance_from_point(self.__triangle_list[2]) + self.__triangle_list[0].distance_from_point(self.__triangle_list[2])


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
