import string
import random
import re


def generate_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


def password_secure(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@*_])[A-Za-z\d@*_]{10,}$"
    return re.match(pattern, password) is not None


def validate_customize_password(password):
    if not password_secure(password):
        raise ValueError("❌ Please enter a valid password that meets the requirements")


def main():
    while True:
        password = generate_password()
        print("\n 🔒 Auto_Generated Password: ", password)
        print("\n")

        user_customize = input(
            "Are you satisfied with this password ? \n"
            "1. ✅ Yes , use this password. \n"
            "2. 🔄 Regenerate again . \n"
            "3. ✏️ No, I want to create my own password. \n"
            "\n"
            "Choose 1|2|3 : "
        ).strip()


        if user_customize == '1':
            print("🎉 Your final password : ", password)
            break
        elif user_customize == '2':
            print("Generating a new password...")
            continue
        elif user_customize == '3':
            while True:
                custom_password = input(
                    "\n Create a password with : \n"
                    "- Minimum 10 character \n"
                    "- At least 1 lowercase (a-z),1 uppercase (A-Z) \n"
                    "- At least 1 digit (0-9) and 1 special character (@*_)\n"
                    "Enter you password : "
                ).strip()

                try:
                    validate_customize_password(custom_password)
                    print("\n 🎉 Your custom password is : ", custom_password)
                    confirm = input("Want to continue with this word [YES / NO]: ").strip()

                    if confirm == 'YES':
                        print("\n ✅ Password Confirmed. \n"
                              "Your final password is :", custom_password)
                        break
                    else:
                        print("🔁 Okay, Try again : ")
                        continue

                except ValueError as e:
                    print(e)

            break
        else:
            print("Invalid option . Please enter 1 , 2 or 3.")


if __name__ == "__main__":
    main()
