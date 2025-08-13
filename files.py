from json import dump


def read_employees(file_path: str) -> list:
    number = 0
    employees = []
    with open(file_path, "r", encoding="UTF-8") as file:
        for line in file:
            if number != 0:
                # print(line.strip())
                parts = line.strip().split(",")
                id = int(parts[0])
                name = parts[1]
                salary = int(parts[2])
                employee = {"id": id, "name": name, "salary": salary}
                employees.append(employee)
            number += 1
    return employees


result = read_employees("employees.csv")
print(result)

with open("employees.json", "w", encoding="UTF-8") as file:
    dump(result, file, indent=4, ensure_ascii=False)
