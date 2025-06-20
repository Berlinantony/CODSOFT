import random
import string

def generate_password():
    print("Welcome! Let's create a strong password for you.")

    while True:
        try:
            length = int(input("How many characters should your password have? Enter a number: "))
            if length <= 0:
                print("Please enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("That doesn't look like a number. Try again!")

    use_upper = input("Do you want capital letters in your password? (yes or no): ").strip().lower()
    use_lower = input("Do you want small letters in your password? (yes or no): ").strip().lower()
    use_numbers = input("Should your password include numbers? (yes or no): ").strip().lower()
    use_symbols = input("Want to include special symbols like @, #, or $? (yes or no): ").strip().lower()

    all_characters = ""

    if use_upper == "yes":
        all_characters += string.ascii_uppercase
    if use_lower == "yes":
        all_characters += string.ascii_lowercase
    if use_numbers == "yes":
        all_characters += string.digits
    if use_symbols == "yes":
        all_characters += string.punctuation

    if not all_characters:
        print("You must choose at least one character type to create a password.")
        return

    password = ''.join(random.choice(all_characters) for _ in range(length))

    print("\nYour new secure password is:")
    print(f"{password}")

generate_password()
