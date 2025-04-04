import random, string
uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)
symbols = list(string.punctuation)

def generate_password(password_length):
    new_password = ''
    while len(new_password) < password_length:
        rand_uppercase = random.choice(uppercase_letters)
        rand_lowercase = random.choice(lowercase_letters)
        rand_symbol = random.choice(symbols)
        random_selection = random.randint(0,2)

        if random_selection == 0:
            new_password += rand_uppercase
        elif random_selection == 1:
            new_password += rand_lowercase
        elif random_selection == 2:
            new_password += rand_symbol

    return new_password


def main():
    print("Welcome to the Password Generator!")
    # Ask user for options here
    password_length = int(input("What's the length of the password?: "))

    # Call generate_password()
    password = generate_password(password_length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()