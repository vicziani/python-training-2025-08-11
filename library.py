def input_choice() -> int:
    print("1. Könyv hozzáadása")
    print("2. Könyvek listázása")
    print("3. Könyv keresése ISBN alapján")
    print("99. Kilépés")

    choice = input("Válassz egy menüpontot: ")
    return int(choice)


def input_book() -> dict:
    isbn = input("ISBN: ")
    author = input("Szerző: ")
    title = input("Könyv címe: ")

    return {"title": title, "author": author, "isbn": isbn}


books = {}
while True:
    choice = input_choice()
    if choice == 1:
        book = input_book()
        books[book["isbn"]] = book

    if choice == 99:
        break
