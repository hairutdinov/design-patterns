class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id}. {self.name}"


class PersonFactory:
    person_id = 0

    def create_person(self, name):
        p = Person(self.person_id, name)
        self.person_id += 1
        return p


pf = PersonFactory()
print(pf.create_person("John"))
print(pf.create_person("Linda"))
print(pf.create_person("Bernard"))
