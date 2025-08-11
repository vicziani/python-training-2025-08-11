names = ["John", "Michael", "Bob"]
for name in names:
    print(f"Hello {name}!")

honapok = [
    "január", "február", "március", "április", "május", "június",
    "július", "augusztus", "szeptember", "október", "november", "december"
]

i = 0
for honap in honapok:
    i += 1
    print(f"Az év egyik hónapja {honap}")
    print(f"Az év {i}. hónapja: {honap}")

numbers = [1, 2, 3, 4]
total = 0
for number in numbers:
    total += number
print(f"Összeg: {total}")

result = ""
for number in numbers:
    result += f"{number}, "
print(result)

print("hello", end="")
print("world")

print("hello \r\n world")