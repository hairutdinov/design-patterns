"""
Motivation:
    - Complicated objects (e.g., cars) aren't designed from scratch
    - An existing (partially or fully constructed) design is a Prototype
    - We make a copy (clone) the prototype and customize it

Prototype - a partially or fully initialized object that you copy (clone)
and make use of.
"""
import copy


class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class Person:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f"{self.name} lives at {self.address}"


john = Person("John", Address("123 London Road", "London", "UK"))
jane = copy.deepcopy(john)
jane.address.street_address = "123B London Road"
print(john)
print(jane)
