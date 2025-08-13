from library import format_book


def test_print_books():
    book = {
        "isbn": "0123456789",
        "title": "Programming in Python",
        "author": "John Doe",
    }
    result = format_book(book)
    assert result == "0123456789: Programming in Python (John Doe)"
