def print_name():
    print("John Doe")
    print("Python Developer")


def print_employee(name: str, position: str = "Unknown"):
    print(type(position))
    print(f"Name: {name}")
    print(f"Position: {position}")


def is_even(n: int) -> bool:
    return n % 2 == 0


print("Start")
print_name()
print_name()

print_employee("John Doe", "Python Developer")
print_employee("Jane Smith", "Data Scientist")

print_employee("Jack Brown")

print("End")

# n = 10
# even = is_even(n)
# if even:
#     print("n is even")

n = 10
if is_even(n):
    print("n is even")

print_employee(position="Python Developer", name="Alice Johnson")
