import unittest
import os
from user_factory import UserFactory
from step_logger import StepLogger
from health_metrics import HealthMetrics

class TestUser(unittest.TestCase):

    def setUp(self):
        self.file_path = "John_data.csv"
        with open(self.file_path, "w") as f:
            f.write("Name,Age,Weight (kg),Height (m),Password,Step Target\n")
            f.write("John,30,70,1.75,password,10000\n")

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_verify_password(self):
        user = UserFactory.get_user("existing", "John", 30, 70, 1.75, "password", 10000)
        self.assertTrue(user.verify_password("password"))

    def test_view_account_details(self):
        user = UserFactory.get_user("existing", "John", 30, 70, 1.75, "password", 10000)
        user.view_account_details()
        # Check manually whether details are correctly printed

    def test_update_details(self):
        user = UserFactory.get_user("existing", "John", 30, 70, 1.75, "password", 10000)
        user.update_details(31, 71, 1.76)
        self.assertTrue(os.path.exists(self.file_path))

class TestStepLogger(unittest.TestCase):

    def setUp(self):
        self.file_path = "John_steps.csv"
        with open(self.file_path, "w") as f:
            f.write("2024-05-03,5000\n")

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_log_steps(self):
        user = UserFactory.get_user("existing", "John", 30, 70, 1.75, "password", 10000)
        step_logger = StepLogger(user)
        step_logger.log_steps(6000)
        self.assertTrue(os.path.exists(self.file_path))

    def test_view_step_log(self):
        user = UserFactory.get_user("existing", "John", 30, 70, 1.75, "password", 10000)
        step_logger = StepLogger(user)
        step_logger.view_step_log()
        # Verify manually if plot is displayed correctly

class TestHealthMetrics(unittest.TestCase):

    def setUp(self):
        self.file_path = "John_data.csv"
        with open(self.file_path, "w") as f:
            f.write("Name,Age,Weight (kg),Height (m),Password,Step Target\n")
            f.write("John,30,70,1.75,password,10000\n")

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_calculate_bmi(self):
        user = UserFactory.get_user("existing", "John", 30, 70, 1.75, "password", 10000)
        health_metrics = HealthMetrics(user)
        result = health_metrics.calculate_bmi()
        self.assertEqual(result, "Your body mass index is: 22.86")

if __name__ == '__main__':
    unittest.main()
