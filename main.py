def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quiz")

def encode(password):
    encoded_password = ""
    for i in str(password):
        i = int(i)
        i += 3
        encoded_password += str(i)

    print("Your password has been encoded and stored!")
    return encoded_password

def decode(encoded_password):
    password = ''
    for i in encoded_password:
        i = int(i)
        password += str(i - 3)

    return password

def main():
    while True:
        menu()
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = int(input("Please enter your password to encode: "))
            encoded_password = encode(password)
            print()
        elif option == 2:
            password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")

        elif option == 3:
            break


if __name__ == "__main__":
    main()

# Hello mei