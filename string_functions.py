def count_vowels(s):
    total = 0
    vowels = "aeiouáéíóőúű"
    for c in s.lower():
        if c in vowels:
            total += 1


def remove_accutes(s):
    accutes = "áéíóőúűÁÉÍÓŐÚŰ"
    without_accutes = "aeioouuAEIOOUU"
    result = ""
    for c in s:
        if c in accutes:
            index = accutes.index(c)
            result += without_accutes[index]
        else:
            result += c
    return result


def check_password(password):
    no_lowers = 0
    no_uppers = 0
    no_digits = 0
    for c in password:
        if c.islower():
            no_lowers += 1
        elif c.isupper():
            no_uppers += 1
        elif c.isdigit():
            no_digits += 1
    return no_lowers > 1 and no_uppers > 1 and no_digits > 1
