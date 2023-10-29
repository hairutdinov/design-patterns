"""
abbreviation - SRP
Also SOC - Separation of Concerns

Idea - if u have a class that class should have its primary responsibility
It should not take other responsibilities

It enforces this idea that a class should have a single reason to change
and that change should be somehow related to its primary responsibility
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self) -> str:
        return "\n".join(self.entries)

    """
    Problem: we are adding secondary responsibility
    Not only does the Journal now store and allow us to manipulate the entries
    but it's now taking on the responsibility of persistence
    by providing func for saving and loading

    If you have other classes that might have their own save and load
    and this func might be centrally changed. If you adopt this approach
    you'll have to go into every class and change their methods

    So you want to take the responsibility of persistence
    and stick it to a separate class
    """
    # def save(self, filename):
    #     with open(filename, 'w') as file:
    #         file.write(str(self))
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as file:
            file.write(str(journal))


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}")


file = "journal.txt"
PersistenceManager.save_to_file(j, file)
