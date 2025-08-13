def input_choice() -> int:
    print("1. Könyv hozzáadása")
    print("2. Könyvek listázása")
    print("3. Könyv keresése ISBN alapján")
    print("4. Könyv keresése cím részlet alapján")
    print("99. Kilépés")

    choice = input("Válassz egy menüpontot: ")
    return int(choice)


def input_book() -> dict:
    isbn = input("ISBN: ")
    author = input("Szerző: ")
    title = input("Könyv címe: ")

    return {"title": title, "author": author, "isbn": isbn}


def print_books(books: list, empty_message: str = "Nincsenek könyvek.") -> None:
    if not books:
        print(empty_message)
        return
    for book in books():
        print(format_book(book))


def input_isbn() -> None:
    return input("Add meg az ISBN-t: ")


def format_book(book: dict) -> str:
    return f"{book['isbn']}: {book['title']} ({book['author']})"


def find_book_by_isbn(books: dict, isbn: str) -> None:
    if not books:
        print("Nincsenek könyvek.")
    elif isbn not in books:
        print("Nem találtam könyvet.")
    else:
        book = books[isbn]
        print(format_book(book))


def find_books_by_part(books: dict, part: str) -> list:
    result = []
    for book in books.values():
        if part.lower() in book["title"].lower():
            result.append(book)
    return result


def input_part() -> str:
    return input("Add meg a cím részletet: ").strip()


if __name__ == "__main__":
    books = {}
    while True:
        choice = input_choice()
        if choice == 1:
            book = input_book()
            books[book["isbn"]] = book
        elif choice == 2:
            print_books(books.values())
        elif choice == 3:
            isbn = input_isbn()
            find_book_by_isbn(books, isbn)
        elif choice == 4:
            part = input_part()
            found_books = find_books_by_part(books, part)
            print_books(found_books, "Nincsenek találatok.")
        elif choice == 99:
            break
        else:
            print("Érvénytelen menüpont, próbáld újra.")
    print("Viszlát!")
