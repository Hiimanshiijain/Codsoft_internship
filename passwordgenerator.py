import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Password length should be greater than 0.")

        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()