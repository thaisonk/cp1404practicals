"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load subject data from file and display it."""
    subjects = load_subject_data(FILENAME)
    display_subjects(subjects)


def load_subject_data(filename=FILENAME):
    """Read subject data from a file and return as a list of lists."""
    subjects = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])  # convert student count to int
            subjects.append(parts)
    return subjects

def display_subjects(subjects):
    """Display subject's details in readable format."""
    for subject_code, lecturer, num_students in subjects:
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")

main()