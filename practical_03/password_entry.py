def main():
    min_length = 5
    password = get_password(min_length)

    password_to_asterisks(password)


def password_to_asterisks(password):
    for i in range(0, len(password)):
        print('*', end=' ')


def get_password(min_length):
    password = input("Please enter a password: ")
    while len(password) < min_length:
        print("Password is not valid")
        password = input("Please enter a password: ")
    return password


main()
