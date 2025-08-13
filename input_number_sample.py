def input_number(message: str) -> int:
    print(message)
    while True:
        try:
            number = int(input())
            return number
        except ValueError:
            print("Kérlek, adj meg egy számot!")


input_number("Add meg az életkorodat: ")
