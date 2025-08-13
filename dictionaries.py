words = {"dog": "kutya", "cat": "macska"}
print(words)

print(words["dog"])  # Keresés kulcs alapján
print(words["cat"])

words["bird"] = "madár"  # Új kulcs-érték pár hozzáadása
words["dog"] = "kutya, kutyus"
print(words)

del words["cat"]  # Kulcs-érték pár eltávolítása
print(words)

# del words["xyz"] # KeyError

print("dog" in words)  # Ellenőrzés, hogy benne van-e a kulcs

for key in words.keys():
    print(f"{key}: {words[key]}")

for key, value in words.items():
    print(f"{key}: {value}")
