#step_logger.py
import matplotlib.pyplot as plt
from datetime import datetime
import csv

class StepLogger:
    def __init__(self, user):
        self.user = user

    def log_steps(self, steps):
        file_path = f"{self.user.name}_steps.csv"
        today = datetime.now().strftime("%Y-%m-%d")
        updated = False

        try:
            rows = []
            with open(file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == today:
                        rows.append([today, steps])
                        updated = True
                    else:
                        rows.append(row)
        except FileNotFoundError:
            rows = []

        if not updated:
            rows.append([today, steps])

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Steps logged for {today}: {steps}")

    def view_step_log(self):
        file_path = f"{self.user.name}_steps.csv"
        dates, steps = [], []
        try:
            with open(file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    dates.append(row[0])
                    steps.append(int(row[1]))

            plt.figure(figsize=(10, 5))
            plt.plot(dates, steps, marker='o', linestyle='-', color='b')
            plt.title(f'Step Log for {self.user.name}')
            plt.xlabel('Date')
            plt.ylabel('Steps')
            plt.xticks(rotation=45)
            plt.axhline(y=self.user.step_target, color='r', linestyle='--', label=f"Target: {self.user.step_target} steps")
            plt.tight_layout()
            plt.show()

        except FileNotFoundError:
            print("No step log found.")
        except ValueError:
            print("Error in log file format. Please ensure it contains valid dates and step counts.")
