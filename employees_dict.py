# employees = {1: "John Doe", 2: "Jack Doe", 3: "Jane Smith"}
# print(employees[2])

# employees = {
#     1: ["John Doe", "Python Developer", 1970],
#     2: ["Jack Doe", "Java Developer", 1985],
# }

# print(employees[2][1])

employee = {
    "name": "John Doe",
    "position": "Python Developer",
    "year_of_birth": 1970,
}

employees = {
    1: {
        "name": "John Doe",
        "position": "Python Developer",
        "year_of_birth": 1970,
    },
    2: {
        "name": "Jack Doe",
        "position": "Java Developer",
        "year_of_birth": 1985,
    },
}

print(employees[2]["position"])  # Kiírja a Jack Doe pozícióját
