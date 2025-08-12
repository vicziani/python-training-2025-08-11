# DRY - don't repeat yourself
for i in range(1, 20):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

for i in range(1, 20):
    if i % 3 == 0:
        print("Fizz", end="")
    if i % 5 == 0:
        print("Buzz", end="")
    if i % 3 != 0 and i % 5 != 0:
        print(i, end="")
    print(", ", end="")

for i in range(1, 20):
    match = False
    if i % 3 == 0:
        print("Fizz", end="")
        match = True
    if i % 5 == 0:
        print("Buzz", end="")
        match = True
    if not match:
        print(i, end="")
    print(", ", end="")
