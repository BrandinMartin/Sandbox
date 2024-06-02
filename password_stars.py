min_length = 8
password = ""

while len(password) < min_length:
    password = input("Enter your password: ")

    if len(password) < min_length:
        print(f"Password must be at least {min_length} characters long. Please try again.")

print('*' * len(password))
