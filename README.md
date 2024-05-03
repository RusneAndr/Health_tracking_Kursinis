# Health Tracking User Management System

This Python application is designed to help users manage their health-related data, empowering them through a suite of integrated tools. These tools include:

1. **Daily Step Tracker**: Gain insights into daily activity levels and set personalized fitness goals.
2. **Body Mass Index (BMI) Calculator**: Calculate your BMI based on profile data.

## To set up the application, follow these steps:

#### 1. Application Download:
1. Download the application package containing the following Python scripts:
   - `user.py`
   - `user_factory.py`
   - `step_logger.py`
   - `health_metrics.py`
   - `main.py`
2. Extract the downloaded package and place all files in the same directory.

#### 2. Library Installation:
1. Verify that all necessary Python libraries are installed on your system.
2. If any libraries are missing, utilize the pip package manager to install them.
3. For example, to install pwinput, open a terminal or command prompt and execute the following command:
```bash
# For terminal
pip install pwinput
```
```bash
# For command prompt
C:\...\...\...\Health_Tracking_System> pip install pwinput
```

### 3. Application Execution:
1.	Launching the application:
- Open a terminal or command prompt and navigate to the directory containing the extracted application files.
- Execute the following command to launch the application:
2.  How to navigate to desired directory through command prompt:
- Check where you extracted application files.
- Open command prompt. (⊞Win + R and type CMD or navigate to Start menu and search for Command Prompt).
- Use command CD (change directory): 
```bash
C:\...\...>cd C:\...\...\...\Health_Tracking_System
```

```bash
# For command prompt
C:\...\...\...\Health_Tracking_System> python main.py 
```
Alternatively, you can use your preferred Python IDE to open and run the main.py script directly.

### 4. User Interaction:
Upon successful program execution, you will be presented with a user interface menu. This menu provides various functionalities for managing your data. Here is a breakdown of each option:

#### Main Menu
This initial menu serves as primary access point for user account management within the application. It offers three key functionalities:
1. **Create New Account**:
- This option allows you to register for a new account within the application. Upon successful registration, you will gain access to all platform features and functionalities. To create a new account, you will be prompted to provide the following details:
  - `Username`
  - `Age`
  - `Weight`
  - `Height`
  - `Daily Step Target`
  - `Password`

- After entering your information and confirming your password, the application will inform you whether your account creation was successful.

2. **Login**:
- This option enables you to access your existing user account. To log in, you will be required to enter your registered username and password. Upon successful login, you will be redirected to your personalized health dashboard where you can manage your data and utilize various application features.
3. **Exit**:
- This option allows you to terminate the application and close the program.

#### Logged-In Menu

Upon successful login, you will be presented with a dedicated menu offering various functionalities for managing your health data:

1. **View Account Details**: Access and review your registered account information, including username, age, weight, height, and daily step target.
2. **Update Account**: Modify your existing account details, allowing you to update your age, weight, height, and daily step target as needed.
3. **BMI Calculator**: Calculate your Body Mass Index (BMI) based on your weight and height. This metric provides with valuable insights into your weight status and potential health risks.
4. **Log Daily Steps**: Record the number of steps you have taken throughout the day. This data contributes to tracking activity levels and progress towards your daily step goals.
5. **View Step Log**: Visualize a graphical representation of your daily step logs over time. This historical data allows you to monitor your activity trends and identify areas for improvement.
6. **Logout**: Terminate your current user session and return to the main menu.


## 4 OOP pillars

This application leverages the core principles of Object-Oriented Programming (OOP) to achieve a robust and maintainable structure. Specifically, it employs:

1. **Encapsulation**: Bundles data and functionality within classes, demonstrated through private attributes and methods.

- Usage in Code: Encapsulation is demonstrated through the use of private attributes and methods, which can only be accessed within the class where they are defined. In our code, the ‘__password’ attribute in the ‘User’ class is encapsulated, and access to it is restricted to the class methods.

```bash
class User:
    def __init__(self, name, age, weight_kg, height_m, password, step_target=10000):
        self.__password = password

    def verify_password(self, provided_password):
        return self.__password == provided_password
```

2. **Polymorphism**: Allows objects of different classes to respond uniquely to the same method calls, achieved through method overriding.

- Usage in Code: Polymorphism is demonstrated in the code through method overriding, where subclasses provide their own implementation of methods inherited from a superclass. For example, in the ‘User’ class and its subclasses (‘New_user’ and ‘Already_user’), the authenticate method is overridden in the ‘Already_user’ subclass to provide specific authentication logic for existing users.

```bash
class User:
    # Other mothods
    def verify_password(self, provided_password):
        return self.__password == provided_password
class Already_user(User):
    def authenticate(self):
    # Authentication logc for existing users
```

3. **Abstraction**: Provides simplified interfaces, such as through abstract classes and methods.
- Usage in Code: Abstraction is exemplified through abstract classes and methods, where the base class provides a blueprint for subclasses to follow without implementing all the details. In our code, the ‘User’ class serves as an abstraction for user management, providing methods for authentication, account creation, and details viewing.

```bash
class User:
    # Other methods
    def view_account_details(self):
      # Abstract method for viewing account details
class New_user(User):
    # Other methods
    def create_account(self):
    # Implementation of abstract method for creating an account
```

4. **Inheritance**: Facilitates code reuse, where subclasses inherit from parent classes.
- Usage in Code: Inheritance is utilized extensively in the program, where subclasses (‘New_user’ and ‘Already_user’) inherit from the ‘User’ superclass. They inherit common attributes and methods such as user details and password verification.

```bash
class User:
    # Attributes and methods common to all
class New_user(User):
    # Inherits from User class and extends functionality
class Already_user(User):
    # Inherits from User class and overrides authentication method
```

## Design Patterns

### Factory Method Pattern
1.	**How it Works**:
- The Factory Method pattern defines an interface for creating an object, but allows subclasses to alter the type of objects that will be created. It provides a way to delegate the instantiation logic to subclasses.
- In this pattern, a superclass contains a method (the factory method) that acts as a factory for creating objects. Subclasses override this method to specify the concrete type of object they want to create.
2.	**Why it's Suitable**:
- In the Health Tracking User Management System, the UserFactory class implements the Factory Method pattern to create instances of User objects.
- This pattern is suitable because it abstracts the process of object creation, allowing different types of users (New_user or Already_user) to be created without exposing the creation logic directly.
- It promotes code extensibility, as new types of users can be easily added by creating subclasses and implementing the factory method accordingly.
- The Factory Method pattern also adheres to the Open/Closed Principle, as it allows for extension (adding new user types) without modifying existing code.
3.	**Implementation**:
- In the program, the UserFactory class serves as the factory, and the get_user method acts as the factory method.
- Subclasses (New_user and Already_user) override the get_user method to specify the type of user they want to create.
- This pattern abstracts the process of user creation and allows for easy extension in the future.

```bash
class UserFactory:
    @staticmethod
    def get_user(user_type, *args, **kwargs):
        if user_type == "new":
            return New_user(*args, **kwargs)
        elif user_type == "existing":
            return Already_user(*args, **kwargs)
        raise ValueError("Invalid user type provided")
```

### Decorator Design Pattern

The provided code implements a decorator, `log_session_duration`, which measures and logs session duration. Decorators allow you to add reusable behavior to functions or methods without modifying their implementation directly.

1.	What is it?:
- Decorator is a structural design pattern that allows behavior to be added to individual objects dynamically, without affecting the behavior of other objects from the same class.
2.	How it Works:
- In Python, decorators are functions that wrap other functions or methods and provide additional functionality before or after the execution of the wrapped function.
- They take a function as input, perform some action (such as logging or validation), and then return a new function that wraps the original function.
3.	Implementation:
- In the provided code, log_session_duration is a decorator function that takes another function (func) as input.
- Inside log_session_duration, a new function wrapper is defined, which wraps around the original function func.
- The wrapper function starts by recording the start time of the session using time.time().
- It then calls the original function func with any arguments (*args and **kwargs), capturing the result.
- After the function execution, it records the end time of the session and calculates the duration.
- Finally, it prints the duration of the session and returns the result of the original function call.

```bash
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
@log_session_duration
def user_menu(user):
```

## Reading from file & writing to file
1.	**Reading User Data from File**:
- When a user logs in (login function in main.py), the program attempts to authenticate the user by reading their data from a CSV file (Already_user.authenticate method).
- The authenticate method opens the user's data file ({username}_data.csv), reads the file using csv.reader, and checks if the provided username and password match any entry in the file.

2.	**Writing User Data to File**:
- When a new user creates an account (create_account function in main.py), their account details are written to a CSV file (New_user.create_account method).
- The create_account method opens or creates the user's data file ({username}_data.csv), writes the user's details using csv.writer, and saves the file.

3.	**Logging Steps to File**:
- When a user logs their daily steps (log_steps method in StepLogger class), the program logs the steps to a separate CSV file ({username}_steps.csv).
- The log_steps method reads existing step data from the file, updates it with the new steps for the current date, and then writes the updated data back to the file.

4.	**Viewing Step Log from File**:
- When a user views their step log (view_step_log method in StepLogger class), the program reads the step data from the user's step log file.
- The view_step_log method opens the step log file ({username}_steps.csv), reads the data using csv.reader, and plots the steps over time using Matplotlib.

## Core Functionality Unit Testing in Health Tracking System

To ensure the reliability of the health tracking system, core functionalities are tested using the unittest framework. This testing framework helps verify that individual components operate as expected. Here’s an explanation of how the core functionality is covered with unit tests.

### 1. Test Structure
The tests are divided into three categories, aligning with the main components of the system:

1. TestUser: Tests functionalities associated with user accounts.
2. TestStepLogger: Tests functionalities related to logging daily steps.
3. TestHealthMetrics: Tests functionalities associated with health metrics, such as calculating BMI.

Each class contains setUp and tearDown methods to prepare and clean up the environment for testing, ensuring tests run independently of each other.

### 2. Test Cases for User Functionality
**TestUser class focuses on the user-related features**:

- **setUp and tearDown**: These methods handle creating and deleting a mock user file, ensuring tests do not interfere with actual data.

```bash
def setUp(self):
    self.file_path = "John_data.csv"
    with open(self.file_path, "w") as f:
        f.write("Name,Age,Weight (kg),Height (m),Password,Step Target\n")
        f.write("John,30,70,1.75,password,10000\n")

def tearDown(self):
    if os.path.exists(self.file_path):
        os.remove(self.file_path)
```
- **test_verify_password**: This tests whether the system correctly verifies the user's password. It uses the `assertTrue` method to validate the outcome.

```bash
def test_verify_password(self):
    user = UserFactory.get_user("existing", "John", 30, 70, 1.75, "password", 10000)
    self.assertTrue(user.verify_password("password"))
```

- **test_view_account_details**: This method checks if account details are printed correctly. Although manual verification is needed, it ensures the function performs as expected.

```bash
def test_view_account_details(self):
    user = UserFactory.get_user("existing", "John", 30, 70, 1.75, "password", 10000)
    user.view_account_details()
```

- **test_update_details**: This method tests if account details can be updated successfully. It checks the existence of the updated file using `assertTrue`.

```bash
def test_update_details(self):
    user = UserFactory.get_user("existing", "John", 30, 70, 1.75, "password", 10000)
    user.update_details(31, 71, 1.76)
    self.assertTrue(os.path.exists(self.file_path))
```

### 3. Test Cases for Step Logger
**`TestStepLogger` class focuses on logging daily steps**:

- **test_log_steps**: this method tests logging steps by checking if the steps file exists after logging.
```bash
def test_log_steps(self):
    user = UserFactory.get_user("existing", "John", 30, 70, 1.75, "password", 10000)
    step_logger = StepLogger(user)
    step_logger.log_steps(6000)
    self.assertTrue(os.path.exists(self.file_path))
```
- **test_view_step_log**: this method tests viewing the step log, verifying manually whether the plot is correctly displayed.
```bash
def test_view_step_log(self):
    user = UserFactory.get_user("existing", "John", 30, 70, 1.75, "password", 10000)
    step_logger = StepLogger(user)
    step_logger.view_step_log()
```
### 4. Test Cases for Health Metrics
**The TestHealthMetrics class focuses on health-related calculations, like BMI.**
- **test_calculate_bmi**: this method tests calculating the BMI, verifying the result using `assertEqual`.
```bash
def test_calculate_bmi(self):
    user = UserFactory.get_user("existing", "John", 30, 70, 1.75, "password", 10000)
    health_metrics = HealthMetrics(user)
    result = health_metrics.calculate_bmi()
    self.assertEqual(result, "Your body mass index is: 22.86")
```
### 5. Running the Tests
**To execute the tests, the `unittest` framework is used directly by calling `unittest.main()`**:
```bash
if __name__ == '__main__':
    unittest.main()
```

## Results
- **Design Complexity**: Implementing the system with robust OOP principles and design patterns required thoughtful planning, especially when managing the interplay between different user types and their functionalities.
- **Data Integrity**: Ensuring that the system securely handled user credentials and health data while maintaining data integrity across multiple file operations was challenging.
- **Testing Scope**: Balancing the coverage of unit tests with the need for robust and maintainable code posed challenges, especially when simulating different user scenarios and validating graphical outputs.

## Conclusions
The Health Tracking User Management System successfully achieved its goal of providing a comprehensive platform for users to manage their health-related data. The key findings from this coursework highlighted the importance of utilizing OOP principles and design patterns for building maintainable and extensible software. The system offers features such as step tracking, BMI calculation, and user account management, all of which contribute to promoting healthy lifestyles and providing personalized health insights.

### Key Achievements:
- **User-Friendly Design**: The program offers an intuitive user interface and a suite of functionalities that cater to diverse health tracking needs.
- **Modular Architecture**: The use of OOP principles such as encapsulation, polymorphism, abstraction, and inheritance has created a modular and easily extendable codebase.
- **Secure User Management**: The system ensures secure handling of user credentials and data, addressing key privacy concerns.
### Future Prospects:
- **Feature Expansion**: The application can be expanded to include additional health metrics or integrations with wearable devices, enhancing its utility.
- **Scalability**: The current system is designed for individual users, but it can be scaled up to support multiple users or even integrated with larger health platforms.
- **Mobile Integration**: Future developments could involve creating a mobile version of the application, increasing accessibility and user engagement.
