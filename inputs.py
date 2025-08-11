name = input("Mi a neved?")
print(name)
print("Hello", name, "!")
print("Hello ", name, "!", sep="")
print("Hello " + name + "!")
print(f"Hello {name}!")
print("Hello {name}!")
print(f"Hello '{name}'!")
print(f"Hello \"{name}\"!")
print(f'Hello "{name}"!')

n = input("Mondj egy számot!")
print(type(n))
print(2 * int(n))

print(10 * "hello")

# 5
# 2 * 5 = 10

result = 2 * int(n)
print(f"2 * {n} = {result}")