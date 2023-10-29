"""
OCP - Open Closed Principle

OCP suggests that when you add new func,
you add it via extension, not via modification

OCP = open for extension, closed for modification

When we write filter_by_color, and then added filter_by_size in ProductFilter,
we're modifying

After you written and tested class, you should not modify it,
instead you should extend it
"""
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        # return [p for p in products if p.color == color]
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p


apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
print("Green products (old):")
for p in pf.filter_by_color(products, Color.GREEN):
    print(f" - {p.name} is green")


"""
2 criteria filter gives us a total of 3 different methods (possibly more):
color and size = c, s, c & s, c | s

3 criteria -> 7 methods

Changing this example: whenever we add new filter, we add them through
extension, not modification.

We will do it with Enterprise pattern - Specification
"""


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color
        pass


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args: Specification):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item


bf = BetterFilter()
green_spec = ColorSpecification(Color.GREEN)
print("Green products (new):")
for p in bf.filter(products, green_spec):
    print(f" - {p.name} is green")

print("Large products (new):")
large_spec = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large_spec):
    print(f" - {p.name} is large")

print("Large Blue products (new):")
# large_blue_and_spec = AndSpecification(ColorSpecification(Color.BLUE), large_spec)
large_blue_and_spec = ColorSpecification(Color.BLUE) & large_spec
for p in bf.filter(products, large_blue_and_spec):
    print(f" - {p.name} blue large")
