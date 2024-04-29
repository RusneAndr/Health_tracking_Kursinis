#user.py
#User class and its subclasses

import csv

class User:
    def __init__(self, name, age, weight_kg, height_m, password, step_target=0):
        self.name = name
        self.age = age
        self.weight_kg = weight_kg
        self.height_m = height_m
        self.__password = password
        self.step_target = step_target

    def verify_password(self, provided_password):
        return self.__password == provided_password

    def view_account_details(self):
        file_path = f"{self.name}_data.csv"
        try:
            with open(file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(f"Username: {row['Name']}")
                    print(f"Age: {row['Age']}")
                    print(f"Weight: {row['Weight (kg)']} kg")
                    print(f"Height: {row['Height (m)']} m")
                    print(f"Step Target: {row['Step Target']} steps")
        except FileNotFoundError:
            print("Error: Data file not found.")

    def update_details(self, new_age, new_weight, new_height, new_step_target=None):
        self.age = new_age
        self.weight_kg = new_weight
        self.height_m = new_height
        if new_step_target is not None:
            self.step_target = new_step_target
        self.save_to_file(f"{self.name}_data.csv")

    def save_to_file(self, file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            headers = ['Userame', 'Age', 'Weight (kg)', 'Height (m)', 'Password', 'Step Target']
            writer.writerow(headers)
            user_data = [self.name, self.age, self.weight_kg, self.height_m, self.__password, self.step_target]
            writer.writerow(user_data)

class New_user(User):
    def create_account(self):
        self.save_to_file(f"{self.name}_data.csv")
        print("Your account has been created successfully!")


class Already_user(User):
    def authenticate(self):
        file_path = f"{self.name}_data.csv"
        try:
            with open(file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                headers = next(reader)
                for row in reader:
                    if row[0] == self.name and self.verify_password(row[4]):
                        print("Authentication successful! Welcome back.")
                        return True
                print("Authentication failed! Please check your credentials and try again.")
                return False
        except FileNotFoundError:
            print("User file does not exist.")
            return False
