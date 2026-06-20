#Time Converter
#For Mini Strava

import json
import datetime

class Run:
    count = 0
    runs = []


    def __init__(self, date, time, distance):
        self.date = date
        self.time = time
        self.distance = distance
        Run.count += 1
        Run.runs.append(self)

    def calculated_pace(self):
        new_time = self.time / 60
        pace = new_time / self.distance
        return pace

    @classmethod
    def get_count(cls):
        return f"{cls.count}"


    def __str__(self):
        return f"Run on {self.date} | {self.distance} km | Pace: {self.calculated_pace():.2f} minute/km "



# === For Date ===
while True:

    now = datetime.datetime.now()
    date_today = str(now.strftime("%B %d, %Y"))


    # === For User's Distance ===
    user_distance = float(input("How many Km(s) are you gonna run?: "))
    final_distance = float(user_distance)

    # === STOP WATCH LOGIC ===


    user_start = input("Press Enter to Start Run: ")
    start_time = datetime.datetime.now()
    formatted_time = start_time.strftime("%I:%M:%S %p")
    print(f"Time Started: {formatted_time}")

    user_stop = input("Press Enter to Stop Run: ")
    stop_time = datetime.datetime.now()
    formatted_stop = stop_time.strftime("%I:%M:%S %p")
    print(f"Running Stopped: {formatted_stop}")


    # === Get The Cleaner Time ===
    duration = stop_time - start_time
    clean_duration = str(duration).split('.')[0]

    # === Get Total Seconds ===
    clean_seconds = float(duration.total_seconds())

    # === Putting the values in the class ===
    complete_run = Run(date_today, clean_seconds, final_distance)
    final_pace = float(complete_run.calculated_pace())



    print(f"Run Time: {clean_duration} | Pace: {final_pace:.2f} minute/km ")

    print(f"How many runs: {Run.count}")

    print(f"{complete_run}")

    print("\n=== MY RUNNING HISTORY ===")
    for single_run in Run.runs:
        print(single_run)


