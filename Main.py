def register():
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

        with open("users.txt", "a") as file:
            file.write(username + "," + password + "\n")

        print("✅ Registered successfully")

    except Exception as e:
        print("Error during registration:", e)


def login():
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

        with open("users.txt", "r") as file:
            users = file.readlines()

        found = False

        for user in users:
            u, p = user.strip().split(",")
            if u == username and p == password:
                found = True
                break

        if found:
            print("✅ Login successful")
        else:
            print("❌ Invalid credentials")

    except FileNotFoundError:
        print("⚠️ No users registered yet. Please register first.")

    except Exception as e:
        print("Error during login:", e)


def get_number():
    while True:
        try:
            num = int(input("Enter a number: "))
            print("✅ You entered:", num)
            break
        except ValueError:
            print("❌ Invalid input. Enter a number only.")


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Enter Number")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            get_number()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
