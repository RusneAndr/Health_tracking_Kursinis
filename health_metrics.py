#health_metrics.py
#HealthMetrics class for calculating bmi

import csv

class HealthMetrics:
    def __init__(self, user):
        self.user = user

    def calculate_bmi(self):
        file_path = f"{self.user.name}_data.csv"
        try:
            with open(file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    weight_kg = float(row['Weight (kg)'])
                    height_m = float(row['Height (m)'])
                    bmi = weight_kg / (height_m ** 2)
                    return f"Your body mass index is: {bmi:.2f}"
        except FileNotFoundError:
            return "Error: Data file not found."
        except ValueError:
            return "Error: Invalid data in file."
