def passwordcomplexity(input_string):
    n = len(input_string)

    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False
    normalchar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    for char in input_string:
        if char.islower():
            hasLower = True
        if char.isupper():
            hasUpper = True
        if char.isdigit():
            hasDigit = True
        if char not in normalchar:
            specialChar = True

    print("Strength of Password:-", end=" ")
    if (hasLower and hasUpper and hasDigit and specialChar and n>=8):
        print("Strong")
    elif((hasUpper and hasLower) and hasDigit and specialChar and n>=6):
        print("Moderate")
    else:
        print("Weak")

input_string=input("Enter a Password: ")
passwordcomplexity(input_string)