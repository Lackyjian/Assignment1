def to_uppercase(str1):
    num_upper = 0
    for letter in str1[0:4]: 
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1

print(to_uppercase('Lakshay'))
print(to_uppercase('LaKsHaY'))
