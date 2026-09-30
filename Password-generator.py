import random
import string

print("       PASSWORD GENERATOR")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length must be at least 4.")
else:
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    all_characters = string.ascii_letters + string.digits + string.punctuation

    remaining = ''.join(random.choice(all_characters)
                        for i in range(length - 4))

    password = upper + lower + digit + special + remaining

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    print("Generated Password:", password)
    print("Password generated successfully!")