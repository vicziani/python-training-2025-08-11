names = ["Alice", "Bob", "Charlie", "Diana"]
numbers = [1, 2, 3, 4]

mixed = ["Alice", 42, "Bob", 3.14]  # Nem javasolt

print(names[2])

print(numbers[::-1])  # Slicing

for name in names:
    print(name)

names[1] = "Bobby"  # Lista módosítása

print(names)

numbers[1:3] = [105, 106]
print(numbers)

print(len(names))

print([1, 2] + [3, 4])  # Lista összefűzés
print([1, 2] * 3)  # Lista ismétlése

print("Alice" in names)  # Ellenőrzés, hogy benne van-e a lista

names.append("Eve")  # Elem hozzáadása
print(names)

del names[2]  # Elem eltávolítása
print(names)

names.remove("Alice")  # Elem eltávolítása név alapján
print(names)

names = ["ádám", "ÁDÁM", "éva", "ÉVA", "béla", "BÉLA", "CILI"]
names.sort()  # Lista rendezése
print(names)

numbers = [1, 2, 11, 12]
numbers.sort()  # Számok rendezése
print(numbers)

strings = ["1", "2", "11", "12"]
strings.sort()  # Sztringek rendezése
print(strings)

# Tuple - immutable

names = ("Alice", "Bob", "Charlie")
