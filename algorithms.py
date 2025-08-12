numbers = [1, -2, 3, -4, 5]

# Feladat: Add össze a pozitív számokat

total = 0
for number in numbers:
    if number > 0:
        total += number

print("A pozitív számok összege:", total)

# Add össze a számok abszolútértékét!
total = 0
for number in numbers:
    if number < 0:
        total -= number
    else:
        total += number

print("A számok abszolútértékeinek összege:", total)

# Menürendszer

print("Válassz egy műveletet:")
print("1. Könyvek listája")
print("2. Könyv hozzáadása")

choice = input("Választás: ")
if choice == "1":
    print("Könyvek listája:")
    # Itt lenne a könyvek listázása
elif choice == "2":
    print("Könyv hozzáadása:")

# Dinamikus menürendszer
menu = ["Könyvek listája", "Könyv hozzáadása", "Könyv törlése"]
index = 1
for menu_item in menu:
    print(index, menu_item)
    index += 1
selected_option = int(input("Válassz egy műveletet!"))

index = 1
for menu_item in menu:
    if index == selected_option:
        print(f"Te a(z) {menu_item} műveletet választottad.")
    index += 1
