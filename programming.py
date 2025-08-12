# Programozási tételek

# Összegzés tétele
numbers = [2, -3, 4, -5, 6, -7]

total = 0
for number in numbers:
    total += number

print("Összeg:", total)

# Számlálás tétele
# Számoljuk meg, hány pozitív szám van a listában

count = 0
for number in numbers:
    if number > 0:
        count += 1

print("Pozitív számok száma:", count)

# Szélsőérték keresés tétele
# Keressük meg a legnagyobb számot a listában

max_value = numbers[0]
for number in numbers:
    if number > max_value:
        max_value = number

print("Legnagyobb szám:", max_value)

# Eldöntés tétele
# Döntsük el, hogy van-e negatív szám a listában

has_negative = False
for number in numbers:
    if number < 0:
        has_negative = True
        break

# Szűrés
# Keressük ki a pozitív számokat egy új listába
positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)

print("Pozitív számok:", positive_numbers)

# Transzformáció
# Készítsünk egy új listát, amely a számok négyzeteit tartalmazza
squared_numbers = []
for number in numbers:
    squared_numbers.append(number**2)

print("Négyzetszámok:", squared_numbers)
