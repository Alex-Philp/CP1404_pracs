def main():
    MIN_LENGTH = 5
    password = get_password(MIN_LENGTH)

    password_to_asterisks(password)


def password_to_asterisks(password):
    for i in range(0, len(password)):
        print('*', end=' ')


def get_password(MIN_LENGTH):
    password = input("Please enter a password: ")
    while len(password) < MIN_LENGTH:
        print("Password is not valid")
        password = input("Please enter a password: ")
    return password


main()