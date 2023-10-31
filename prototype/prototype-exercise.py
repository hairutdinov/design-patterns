class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.start} : {self.end}"

    def deep_copy(self):
        new_start = Point(self.start.x, self.start.y)
        new_end = Point(self.end.x, self.end.y)
        return Line(new_start, new_end)


line = Line(Point(2, 3), Point(5, 4))
line_copy = line.deep_copy()
line_copy.end.x = 6
print(line)
print(line_copy)
