class Field:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def __str__(self):
        return "self.%s = %s" % (self.type, self.name)


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def add_field(self, type, name):
        self.fields.append(Field(type, name))
        return self

    def __str__(self):
        lines = ["class %s:" % self.name]
        indent = "  "
        if len(self.fields) > 0:
            lines.append("%sdef __init__(self):" % indent)
            indent += "  "
            for f in self.fields:
                lines.append("%s%s" % (indent, f))
        else:
            lines.append("%spass" % indent)

        return "\n".join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self._class = Class(root_name)

    def add_field(self, type, name):
        return self._class.add_field(type, name)

    def __str__(self):
        return self._class.__str__()


cb = CodeBuilder("Person").add_field("name", '""').add_field("age", "0")
# cb = CodeBuilder('Person')
print(cb)
