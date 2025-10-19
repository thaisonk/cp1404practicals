"""
CP1404 Prac
Hexadecimal Colour Lookup Program
"""

COLOUR_CODES = {"absolutezero": "#0048ba",
                "acidGreen": "#b0bf1a",
                "aliceblue": "#f0f8ff",
                "alizarincrimson": "#e32636",
                "amaranth": "#e52b50",
                "amber": "#ffbf00",
                "amethyst": "#9966cc",
                "antiqueWhite": "#faebd7",
                "aqua": "#00ffff",
                "arylideyellow": "#e9d66b"}

colour_name = input("Enter colour name: ").lower() # Input is case insensitive

while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_CODES[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").lower()
