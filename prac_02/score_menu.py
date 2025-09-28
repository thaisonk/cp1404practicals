"""
CP1404/CP5632 - Practical
Program with menu to manage scores
"""

def main():
    """Main program loop with menu"""
    score = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Choose an option: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            print(show_stars(score))
        elif choice == "Q":
            print("Farewell")
            break
        else:
            print("Invalid choice, please try again.")


def get_valid_score() -> int:
    """Prompt user until a valid score (0-100) is entered"""
    while True:
        try: # Try and except prevents non integer values from creating a value error
            score = int(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def determine_score_status(score: int) -> str:
    """Return status of the score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score: int):
    """Return as many stars as the score"""
    return "*" * score


main()
