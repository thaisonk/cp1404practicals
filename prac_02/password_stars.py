"""Password Check with Functions"""

def main():
    MIN_LENGTH = 6

    password = input("Enter a password: ")
    password = get_password(MIN_LENGTH, password)

    print_asterisks(password)


def get_password(MIN_LENGTH: int, password: str) -> str:
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password


def print_asterisks(password: str):
    print("*" * len(password))


main()
