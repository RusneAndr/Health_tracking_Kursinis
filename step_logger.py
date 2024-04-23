#step_logger.py
#StepLogger class for logging steps

import matplotlib.pyplot as plt
from datetime import datetime
import csv
import os

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
        data_file_path = f"{self.user.name}_data.csv"
        dates, steps = [], []
        try:
            if os.path.exists(data_file_path):
                with open(data_file_path, mode='r', newline='') as data_file:
                    reader = csv.DictReader(data_file)
                    for row in reader:
                        step_target = int(row.get('Step Target', 0))  # Get step target from the first row
                        break  # Stop after reading the first row
            
            # Read step log
            with open(file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    dates.append(row[0])
                    steps.append(int(row[1]))

            plt.figure(figsize=(15, 8))
            plt.plot(dates, steps, marker='o', linestyle='-', color='b') # Blue line for daily steps
            plt.title(f'Step Log for {self.user.name}')
            plt.xlabel('Date')
            plt.ylabel('Steps')
            plt.xticks(rotation=90)
            plt.axhline(y=step_target, color='r', linestyle='--', label=f"Step Target: {step_target} steps") # Red dashed line for step target
            plt.legend(fontsize='large')
            plt.grid(True)
            plt.tight_layout()
            plt.show()

        except FileNotFoundError:
            print("No step log found.")
        except ValueError:
            print("Error in log file format. Please ensure it contains valid dates and step counts.")
    