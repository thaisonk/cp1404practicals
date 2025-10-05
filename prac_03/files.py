# 1. Ask user for their name and write to name.txt
name = input("Enter your name: ")
name_file = open("name.txt", "w")
name_file.write(name)
name_file.close()


# 2. Read name from name.txt using read() and print greeting
name_file = open("name.txt", "r")
name_from_file = name_file.read().strip()
name_file.close()
print(f"Hi {name_from_file}!")


# 3. Read first two numbers from numbers.txt using readline() and add
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline())
    second_number = int(numbers_file.readline())
print(first_number + second_number)


# 4. Sum all numbers in numbers.txt
total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        total += int(line.strip())
print(total)