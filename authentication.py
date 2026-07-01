import json
import os
import getpass


class Authentication:

    def __init__(self):

        self.file_name = "users.json"
        self.max_attempts = 3

        self.load_users()

    # -------------------------
    # Load Users
    # -------------------------
    def load_users(self):

        if not os.path.exists(self.file_name):

            default_user = {
                "admin": "admin123"
            }

            with open(self.file_name, "w") as file:

                json.dump(default_user, file, indent=4)

        with open(self.file_name, "r") as file:

            self.users = json.load(file)

    # -------------------------
    # Save Users
    # -------------------------
    def save_users(self):

        with open(self.file_name, "w") as file:

            json.dump(self.users, file, indent=4)

    # -------------------------
    # Login
    # -------------------------
    def login(self):

        attempts = self.max_attempts

        print("=" * 60)
        print(" SMART INVENTORY & SALES MANAGEMENT SYSTEM ")
        print("=" * 60)

        while attempts > 0:

            username = input("Username : ")

            password = getpass.getpass("Password : ")

            if username in self.users:

                if self.users[username] == password:

                    print("\nLogin Successful!")
                    print(f"Welcome {username.title()}.")

                    return True

            attempts -= 1

            print("\nInvalid Username or Password.")

            if attempts > 0:

                print(f"Attempts Left : {attempts}")

        print("\nMaximum Login Attempts Reached.")
        print("Exiting Program...")

        return False

    # -------------------------
    # Change Password
    # -------------------------
    def change_password(self):

        username = input("Enter Username : ")

        if username not in self.users:

            print("User Not Found.")
            return

        old_password = getpass.getpass("Old Password : ")

        if self.users[username] != old_password:

            print("Incorrect Password.")
            return

        new_password = getpass.getpass("New Password : ")

        confirm_password = getpass.getpass("Confirm Password : ")

        if new_password != confirm_password:

            print("Passwords do not match.")
            return

        self.users[username] = new_password

        self.save_users()

        print("\nPassword Changed Successfully.")

    # -------------------------
    # Add New User
    # -------------------------
    def add_user(self):

        username = input("New Username : ")

        if username in self.users:

            print("Username Already Exists.")

            return

        password = getpass.getpass("Password : ")

        self.users[username] = password

        self.save_users()

        print("New User Added Successfully.")

    # -------------------------
    # Display Users
    # -------------------------
    def display_users(self):

        print("\nRegistered Users")

        print("-" * 40)

        for username in self.users:

            print(username)

    # -------------------------
    # Delete User
    # -------------------------
    def delete_user(self):

        username = input("Username : ")

        if username == "admin":

            print("Default Admin Cannot Be Deleted.")

            return

        if username not in self.users:

            print("User Not Found.")

            return

        del self.users[username]

        self.save_users()

        print("User Deleted Successfully.")

    # -------------------------
    # Logout
    # -------------------------
    def logout(self):

        print("\nLogged Out Successfully.")