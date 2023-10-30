"""
Motivation for using:
    - When you need to create complicated objects with complicated constructors
    - When you need to create an objects that require a lot of steps to create
    - When you need to create an object with a lot of attributes

Instead, opt for piecewise construction (компонентное построение)

Builder provides an API for constructing an object step-by-step

Formal defenition:
When piecewise object construction is complicated,
provide an API for doing it succinctly (кратко, лаконично)

"""


class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")

        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))

    # Fluent interface
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

    def clear(self):
        self.__root = HtmlElement(name=self.root_name)

    def __str__(self):
        return str(self.__root)


builder = HtmlBuilder("ul")
builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")
print(builder)
