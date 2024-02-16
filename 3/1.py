# проверка типов объектов в is_intersect (метод один в обоих классах)

from math import sqrt
from uuid import uuid4

class InvalidFigureError(Exception):
    pass

class Point:
    def __init__(self, x, y):
        if not all(isinstance(arg, int) or isinstance(arg, float) for arg in (x, y)):
            raise TypeError("Coords should have int or float type")
        self._x = x
        self._y = y
        self._id = uuid4()

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_id(self):
        return self._id

    def set_x(self, value):
        self._x = value
    
    def set_y(self, value):
        self._y = value

    def get_coords(self):
        return self._x, self._y
    
    def dist(self, p):
        return sqrt((self._x - p.get_x()) ** 2 + (self._y - p.get_y()) ** 2)

class Triangle:
    def __init__(self, p1, p2, p3):
        if not all(isinstance(arg, Point) for arg in (p1, p2, p3)):
            raise TypeError("Points should have Point type")
        p = (p1.dist(p2) + p2.dist(p3) + p3.dist(p1)) / 2 
        if not p * (p - p1.dist(p2)) * (p - p2.dist(p3)) * (p - p3.dist(p1)):
            raise InvalidFigureError("Invalid triangle")
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._id = uuid4()

    def get_p1(self):
        return self._p1
    
    def get_p2(self):
        return self._p2

    def get_p3(self):
        return self._p3
    
    def get_id(self):
        return self._id

    def set_p1(self, value):
        self._p1 = value
    
    def set_p2(self, value):
        self._p2 = value

    def set_p3(self, value):
        self._p3 = value

    def get_points(self):
        return self._p1, self._p2, self._p3

    # двумерный вектор 'v' прикладывается к каждой точке, и на него производится смещение
    def move(self, v):
        if not isinstance(v, list) and not isinstance(v, tuple):
            raise TypeError("Vector v should have tuple or list type")
        for point in (self._p1, self._p2, self._p3):
            point.set_x(point.get_x() + v[0])
            point.set_y(point.get_y() + v[1])

    def is_intersect(self, tetragon):
        pass

class Tetragon(Triangle):
    def __init__(self, p1, p2, p3, p4):
        if not all(isinstance(arg, Point) for arg in (p1, p2, p3, p4)):
            raise TypeError("Points should have Point type")
        # Tetragon center
        cx = sum([point.get_x() / 4 for point in (p1, p2, p3, p4)])
        cy = sum([point.get_y() / 4 for point in (p1, p2, p3, p4)])
        c = Point(cx, cy)
        if not p1.dist(c) == p2.dist(c) == p3.dist(c) == p4.dist(c):
            raise InvalidFigureError("Invalid tetragon") 
        super().__init__(p1, p2, p3)
        self._p4 = p4
        # id уже есть за счет наследования от Triangle

    def get_p4(self):
        return self._p4

    def set_p4(self, value):
        self._p4 = value

    def get_points(self):
        # added comma to create tuple
        return super().get_points() + (self._p4,)

    # двумерный вектор 'v' прикладывается к каждой точке, и на него производится смещение
    def move(self, v):
        if not isinstance(v, list) and not isinstance(v, tuple):
            raise TypeError("Vector v should have tuple or list type")
        super().move(v)
        self._p4.set_x(self._p4.get_x() + v[0])
        self._p4.set_y(self._p4.get_y() + v[1])
    
    def is_intersect(self, triangle):
        pass

# Create Egyptian triangle and move it   
tr = Triangle(Point(0,3),Point(0,0),Point(4,0))
tr.move([1,2])
print([point.get_coords() for point in tr.get_points()])

# Create tetragon and move it
tetr = Tetragon(Point(0,0), Point(0,2), Point(4,0), Point(4,2))
tetr.move([1,2])
print([point.get_coords() for point in tetr.get_points()])
print(tetr.get_id())

# Check if point is valid
try:
    p = Point("1", "2")
except TypeError as e:
    print(e)

# Check if triangle is valid
try:
    tr = Triangle(Point(0,1),Point(0,2),Point(0,3))
except (TypeError, InvalidFigureError) as e:
    print(e)

# Check if tetragon is valid
try:
    tetr = Tetragon(Point(0,1),Point(0,2),Point(0,3),Point(0,4))
except (TypeError, InvalidFigureError) as e:
    print(e)