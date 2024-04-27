import unittest
from unittest.mock import patch, mock_open
import matplotlib.pyplot as plt
import csv

# Assuming these are the structures of your actual classes
class User:
    def __init__(self, username, age, weight, height, password):
        self.username = username
        self.age = age
        self.weight = weight
        self.height = height
        self.password = password
        self.step_target = None  # Assuming step_target can be set outside

    def verify_password(self, password):
        return self.password == password

class New_user(User):
    def create_account(self):
        print("Your account has been created successfully!")
        return True

class Already_user(User):
    def authenticate(self):
        # Here we just return True to simulate successful authentication,
        # Real implementation should check credentials properly.
        return True

class StepLogger:
    def __init__(self, user):
        self.user = user

    def view_step_log(self):
        step_target = self.user.step_target
        plt.axhline(y=step_target, color='r', linestyle='--', label=f"Step Target: {step_target} steps")
        plt.show()

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("JohnDoe", 30, 70, 1.75, "secure123")

    def test_verify_password(self):
        self.assertTrue(self.user.verify_password("secure123"))
        self.assertFalse(self.user.verify_password("wrongpassword"))

class TestNewUser(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open())
    @patch('csv.writer')
    def test_create_account(self, mock_csv_writer, mock_file):
        new_user = New_user("JaneDoe", 28, 65, 1.65, "password")
        self.assertTrue(new_user.create_account())

class TestAlreadyUser(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open(read_data="JaneDoe,28,65,1.65,password"))
    @patch('csv.reader', return_value=iter([["JaneDoe", "28", "65", "1.65", "password"]]))
    def test_authenticate(self, mock_csv_reader, mock_file):
        existing_user = Already_user("JaneDoe", 28, 65, 1.65, "password")
        self.assertTrue(existing_user.authenticate())

class TestStepLogger(unittest.TestCase):
    def setUp(self):
        self.user = User("JohnDoe", 30, 70, 1.75, "secure123")
        self.user.step_target = 15000
        self.step_logger = StepLogger(self.user)

    @patch("matplotlib.pyplot.show")
    @patch("csv.reader", return_value=iter([["2022-04-01", "10000"], ["2022-04-02", "15000"]]))
    @patch("builtins.open", new_callable=mock_open, read_data="2022-04-01,10000\n2022-04-02,15000")
    def test_view_step_log(self, mock_file, mock_csv_reader, mock_plt_show):
        self.step_logger.view_step_log()
        mock_plt_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()