import random, string
uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)
symbols = list(string.punctuation)

def generate_password(password_length, use_upper, use_symbols):
    new_password = ''
    char_pool = [lowercase_letters]

    if use_upper:
        char_pool.append(uppercase_letters)
    if use_symbols:
        char_pool.append(symbols)

    new_password = ""

    for _ in range(password_length):
        selected_set = random.choice(char_pool)
        new_password += random.choice(selected_set)

    return new_password

def main():
    print("Welcome to the Password Generator!")
    # Ask user for options here
    try:
        password_length = int(input("What's the length of the password?: "))
    except ValueError:
        print("Please enter a valid number")

    use_upper = input("Do you want to use uppercase? (Y/N) ")
    use_symbols = input("Do you want to use symbols? (Y/N) ")

    use_upper = use_upper.lower() == 'y'
    use_symbols = use_symbols.lower() == 'y'


    # Call generate_password()
    password = generate_password(password_length, use_upper, use_symbols)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()