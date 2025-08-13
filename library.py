def input_choice() -> int:
    print("1. Könyv hozzáadása")
    print("2. Könyvek listázása")
    print("3. Könyv keresése ISBN alapján")
    print("99. Kilépés")

    choice = input("Válassz egy menüpontot: ")
    return int(choice)


while True:
    choice = input_choice()
    if choice == 99:
        break
