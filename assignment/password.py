import string

def strong(password):
    is_upper = False
    is_lower = False
    is_special = False
    is_digit = False

    for char in password:
        if char.isupper():
            is_upper = True
        elif char.islower():
            is_lower = True
        elif char in string.punctuation:
            is_special = True
        elif char.isdigit():
            is_digit = True

    print("task done")
    return is_upper and is_lower and is_special and is_digit

a = input("Enter your password: ")
result = strong(a) 

if result:
    print("It is a strong password")
else:
    print("It is a weak password")

