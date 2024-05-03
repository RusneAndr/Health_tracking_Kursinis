#main.py
import os
import time
import pwinput
from user_factory import UserFactory
from health_metrics import HealthMetrics
from step_logger import StepLogger

# Decorator design patter to calculate the duration of the session
def log_session_duration(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration_minutes = (end_time - start_time) / 60
        print(f"User session duration: {duration_minutes:.2f} minutes")
        return result
    return wrapper

def main_menu():
    while True:
        print("\nWelcome to the Health Tracking System")
        print("1. Create New Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Thank you for using our system.")
            break
        else:
            print("Invalid choice. Please choose from 1, 2 or 3.")

def create_account():
    name = input("Enter your user name: ")
    if os.path.exists(f"{name}_data.csv"):
        print("Username already exists. Please choose a different username.")
        return
    while True:
        try:
            age = int(input("Enter your age: "))
            weight_kg = float(input("Enter your weight in kg: "))
            height_m = float(input("Enter your height in meters: "))
            step_target = int(input("Enter your daily step target: "))
            password = pwinput.pwinput(prompt="Enter your password: ", mask="*")
            break
        except ValueError:
            print("Invalid input! Please enter numeric values.")

    # Creating a new user using the UserFactory
    new_user = UserFactory.get_user("new", name, age, weight_kg, height_m, password, step_target)
    new_user.create_account()

def login():
    name = input("Enter your name: ")
    password = pwinput.pwinput(prompt="Enter your password: ", mask="*")
   
    # Creating an existing user using the UserFactory
    user = UserFactory.get_user("existing", name, None, None, None, password)
    if user.authenticate():
        user_menu(user)

@log_session_duration
def user_menu(user):
    while True:

        print("\nUser Menu")
        print("1. View Account Details")
        print("2. Update Account")
        print("3. BMI Calculator")
        print("4. Log Daily Steps")
        print("5. View Step Log")
        print("6. Logout")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            user.view_account_details()
        elif choice == '2':
            update_account(user)
            confirm = input("Do you want to see you account details? (yes/no): ").lower()
            if confirm == 'yes':
                user.view_account_details()
        elif choice == '3':
            health_metrics = HealthMetrics(user)
            bmi_result = health_metrics.calculate_bmi()
            print(bmi_result)
        elif choice == '4':
            try:
                steps = int(input("Enter the number of steps taken today: "))
                step_logger = StepLogger(user)
                step_logger.log_steps(steps)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif choice == '5':
            step_logger = StepLogger(user)
            step_logger.view_step_log()
        elif choice == '6':
            print("You have been logged out successfully.")
            break
        else:
            print("Invalid choice. Please choose from 1 to 6.")

def update_account(user):
    while True:
        try:
            new_age = int(input("Enter your new age: "))
            new_weight = float(input("Enter your new weight in kg: "))
            new_height = float(input("Enter your new height in meters: "))
            confirm = input("Do you want to update the step target as well? (yes/no): ").lower()
            if confirm == 'yes':
                new_step_target = int(input("Enter your new daily step target: "))
                user.update_details(new_age, new_weight, new_height, new_step_target)
            else:
                user.update_details(new_age, new_weight, new_height)
            print("Account updated successfully.")
            break
        except ValueError:
            print("Invalid input! Please enter numeric values for age, weight, height, and optionally step target.")

def main():
    main_menu()

if __name__ == "__main__":
    main()
