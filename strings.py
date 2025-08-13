empty = ""
name = "John Doe"

json = """{
    "name": "John",
    "age": 30,
    "city": "New York"
}"""

print(json)

for c in name:
    print(c)

print(name[2])

# Slice

print(name[1:4])  # Output: "ohn"
print(name[1:])  # Output: "ohn Doe"
print(name[:3])  # Output: "Joh"
print(name[::2])
print(name[::-1])  # Output: "eoD nhoJ"

sentence = "indulagorogaludni"
print(sentence == sentence[::-1])

print(len(name))

print("gorog" in sentence)
print("rozsomák" in sentence)

print(sentence.upper())

hungarian = "árvíztűrő tükörfúrógép"
print(hungarian.upper())

print("almakorte".index("korte"))  # Output: 4
# print("almakorte".index("meggy"))
print("almakorte".find("korte"))  # Output: 4
print("almakorte".find("meggy"))  # Output: -1

print("      alma korte meggy ".strip())  # Output: "alma korte meggy"

fruits = "alma,korte,meggy".split(",")
print(fruits)
