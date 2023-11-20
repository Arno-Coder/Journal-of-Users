
users = []

def create_user(user: dict) -> None:

    if not unique_email(user.get('email')):
        print("This email is already registered. Please use a different")

    users.append(user)

def get_user_by_email(email: str) -> dict | None:

    for user in users:
        if user.get('email') == email:
            return user
    return None

def update_user(email: str, data: dict) -> dict | None:

    user = get_user_by_email(email)
    if user is None:
        return None

    for key, value in data.items():
        user[key] = value

    print('User is updated')
    return user

def delete_user(email: str) -> None:

    user = get_user_by_email(email)

    if user is None:
        return None

    users.remove(user)
    print("User deleted successfully.")

def unique_email(email: str) -> bool:

    for user in users:
        if user.get('email') == email:
            return False
    return True


option_list = ["Create User", "Show list of Users", "Delete user from List ", "Authorization", "Exit"]

user_num = 0

while True:
    print("Choose one option:")
    for i in option_list:
        print(f"{int(option_list.index(i)) + 1}. {i}")

    try:
        user_num = int(input("Enter option: "))
    except ValueError:
        print("Invalid option. Please enter a number.")
        continue

    if user_num == 1:

        user = {}
        user['name'] = input("Name: ")
        user['surname'] = input("Surname: ")
        user['age'] = input("Age: ")
        user['address'] = input("Address: ")
        user['email'] = input("Email: ")

        while not unique_email(user.get('email')):
            print("This email is already registered. Please use a different.")
            user['email'] = input("Email: ")

        user['password'] = input("Password: ")
        while len(user['password']) < 8:
            print("Password should be longer.")
            user['password'] = input("Password: ")

        create_user(user)
        print("Account created successfully.")

    elif user_num == 2:

        for user in users:
            print(user)

    elif user_num == 3:

        email = input("Enter the email of the user you want to delete: ")
        delete_user(email)

    elif user_num == 4:

        email = input("Email: ")
        password = input("Password: ")
        user = get_user_by_email(email)

        if user is None:
            print("User not found.")
        elif user.get('password') == password:
            print("Login successful.")
        else:
            print("Invalid action")

    elif user_num == 5:
        print("Good Bye")
        break

    else:
        print("Invalid option. Try again!")