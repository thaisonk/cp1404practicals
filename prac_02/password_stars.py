"""Password Check with Functions"""

def main():
    MIN_LENGTH = 6

    password = get_password(MIN_LENGTH)

    print_asterisks(password)


def print_asterisks(password: str):
    print("*" * len(password))


def get_password(MIN_LENGTH: int) -> str:
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password


main()