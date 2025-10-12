import random

# Constants
NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    num_quick_picks = int(input("How many quick picks? "))

    for _ in range(num_quick_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_PICK:
            num = random.randint(MIN_NUMBER, MAX_NUMBER)
            if num not in quick_pick:  # ensure no duplicates
                quick_pick.append(num)
        quick_pick.sort()  # sort ascending
        print(" ".join(f"{n:2}" for n in quick_pick))

main()
