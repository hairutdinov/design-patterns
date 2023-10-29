"""
LSP - Liskov substitution

The idea is that if you have some interface that takes
some sort of base class, You should be able to stick
a derived class in there and everything should work

__________________________________________________________

принцип подстановки Барбары Лисков.

Для того чтобы следовать принципу подстановки Барбары Лисков
необходимо в базовый (родительский) класс выносить только общую логику,
характерную для классов наследников, которые будут ее реализовывать и,
соответственно, можно будет базовый класс без проблем заменить на его
класс-наследник.

Принцип подстановки Барбары Лисков заключается в правильном использовании
отношения наследования. Мы должны создавать наследников какого-либо базового
класса тогда и только тогда, когда они собираются правильно реализовать его логику,
не вызывая проблем при замене родителей на наследников.
"""


class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc: Rectangle):
    w = rc.width
    # problem in this line of code
    # this line unfortunately has the side effect of changing the width
    rc.height = 10
    expected = int(w * 10)
    print(f"Expected an area of {expected}, got {rc.area}")


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
