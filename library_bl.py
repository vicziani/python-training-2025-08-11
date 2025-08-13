def find_books_by_part(books: dict, part: str) -> list:
    result = []
    for book in books.values():
        if part.lower() in book["title"].lower():
            result.append(book)
    return result
