"""Password Check with Functions"""

def main():
    MIN_LENGTH = 6
    """Get password and print using functions"""
    password = get_password(MIN_LENGTH)

    print_asterisks(password)


def print_asterisks(password: str):
    """Print number of asterisks for characters in password."""
    print("*" * len(password))


def get_password(MIN_LENGTH: int) -> str:
    """Get password with minimum length required."""
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password


main()