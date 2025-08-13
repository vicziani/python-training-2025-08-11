# Histogram a dict egyik felhasználási területe
word = "aaaaaabbbcccbbbbaaaaccc"
counts = {}
for letter in word:
    if letter not in counts:
        counts[letter] = 1
    else:
        counts[letter] += 1

print(counts)
