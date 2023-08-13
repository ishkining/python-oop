from enum import Enum
from math import *


class CoordinateSystemEnum(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return f'{self.x} - {self.y}'

    # def __init__(self, x, y, system=CoordinateSystemEnum.CARTESIAN):
    #     if system == CoordinateSystemEnum.CARTESIAN:
    #         self.x = x
    #         self.y = y
    #     elif system == CoordinateSystemEnum.POLAR:
    #         self.x = x * cos(y)
    #         self.y = x * sin(y)


class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        p = Point()
        p.x = x
        p.y = y
        return p

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))
