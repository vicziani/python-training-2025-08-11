def convert_number():
    number = int("abc")


try:
    convert_number()
except ValueError as e:
    print("Nem szám")
