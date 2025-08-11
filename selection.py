n = int(input("Adj meg egy számot!"))
if n > 0:
    print("pozitív szám")
elif n == 0:
    print("nulla")
else:
    print("negatív szám")

if n % 2 == 0:
    print("páros")
else:
    print("páratlan")

if n < 0:
    print(-n)
else:
    print(n)

if n >= 18:
    print("Nagykorú")
else:
    print("Kiskorú")

a = int(input("Egyik szám?"))
b = int(input("Másik szám?"))

if a < b:
    print(a)
else:
    print(b)

password = input("Mi a jelszó?")
if password == "python123":
    print("Belépett")
else:
    print("Nem belépett")