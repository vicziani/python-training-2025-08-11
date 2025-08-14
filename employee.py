class Employee:
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    def get_age(self):
        return 2025 - self.year_of_birth


e1 = Employee("Alice", 1990)
e2 = Employee("Bob", 1985)

print(e1.name)
print(e2.name)

print(e1.get_age())
