import  re

def is_strong_pasword(password):
    length = re.compile(r'^.{8,}$')
    uppercase = re.compile(r'[A-Z]')
    lowercase = re.compile(r'[a-z]')
    digit = re.compile(r'[0-9]')
    special_char = re.compile(r'[!@#$%^&*()_+{}:;,.<>?~]')

    length_valid = bool(length.match(password))
    uppercase_valid = bool(uppercase.search(password))
    lowercase_valid = bool(lowercase.search(password))
    digit_valid = bool(digit.search(password))
    special_char_valid = bool(special_char.search(password))

    return (length_valid and uppercase_valid and lowercase_valid and digit_valid and special_char_valid)

def main():
    attempts = 3

    while attempts > 0:
        password = input("Please enter a password: ")

        try:
            if is_strong_pasword(password):
                print("Congratulations! Your password is strong")
                break
            else:
                print("Password does not match the criteria")
                print("Password must be: ")
                print("- Be at least 8 characters")
                print("- Must contain at least one uppercase")
                print("- Must contain at least one lowercase")
                print("- Must contain a digit")
                print("- Must contain a symbol")
                attempts -= 1
                if attempts > 0:
                    print(f"You have {attempts} attempts remaining")
                else:
                    print("You have reached a maximum number of attempts")
        except Exception as e:
            print(f"An error occrured: {str(e)}")

if __name__ == "__main__":
    main()