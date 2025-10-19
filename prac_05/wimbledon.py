"""
Wimbledon
Estimate: 35 minutes
Actual: 40 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_CHAMPION = 1
INDEX_COUNTRY = 2

def main():
    """Read data file and print ddetails"""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def process_records(records):
    """Create dictionary of champions and set of countries"""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions:")
    max_len = max(len(name) for name in champion_to_count)
    for name, count in champion_to_count.items():
        print(f"{name:{max_len}} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

def load_records(filename):
    """Load records from file"""
    import csv
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # skip header
        for row in reader:
            records.append(row)
    return records

main()
