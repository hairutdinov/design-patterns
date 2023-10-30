"""
DIP: Dependency Inversion Principle

High level classes should not depend on low level classes.
Both should depend on abstractions.

Abstractions is an interface or abstract class.
You want to depend on abstractions, not on concrete implementations.

Instead of depending on a low level module directly,
we introduced interface RelationshipBrowser
"""
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        raise NotImplementedError


class Relationships(
    RelationshipBrowser
):  # low-level (because it's dealing with things like storage)
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2]


class Research:  # high-level class, cause it uses some other functionality
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}')

    def __init__(self, browser: RelationshipBrowser):
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p.name}")


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

# low-level module
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

# Research(relationships)
Research(relationships)
