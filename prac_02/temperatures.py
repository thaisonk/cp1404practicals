"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = fahrenheit_to_celsius(celsius, fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius(celsius: float, fahrenheit: float) -> float:
    """Convert fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()