"""
Emails
Estimate: 20 minutes
Actual: 27 minutes
"""

def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ").strip()
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()

