import string
import secrets

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    print("Password Generator")

    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            password_length = int(input("Enter the length of each password: "))

            if num_passwords <= 0 or password_length <= 0:
                print("Please enter valid values for number of passwords and password length.")
            else:
                passwords = generate_multiple_passwords(num_passwords, password_length)

                print("\nGenerated Passwords:")
                for i, password in enumerate(passwords, start=1):
                    print(f"{i}. {password}")

                break
        except ValueError:
            print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
