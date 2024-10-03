from datetime import datetime, timedelta

# Define the routine
routine = [
    ("Wake up", "10:00 AM"),
    ("Gym", "11:30 AM - 12:30 PM"),
    ("Shower", "1:00 PM"),
    ("Lunch", "1:40 PM - 2:00 PM"),
    ("Study", "3:00 PM - 4:00 PM"),
    ("Nap", "4:30 PM - 5:30 PM"),
    ("Free time", "5:30 PM - 7:00 PM"),
    ("Dinner", "7:30 PM"),
    ("Netflix/Screen time", "8:00 PM - 10:00 PM"),
    ("Read", "11:00 PM - 12:00 AM"),
    ("TikTok", "12:00 AM - 12:30 AM"),
    ("Sleep", "12:30 AM")
]

# Function to convert time string to datetime object
def convert_to_datetime(time_str):
    return datetime.strptime(time_str, "%I:%M %p")

# Function to display the routine
def display_routine(routine):
    for activity, time in routine:
        if '-' in time:
            start_time, end_time = time.split(' - ')
            start_time = convert_to_datetime(start_time)
            end_time = convert_to_datetime(end_time)
            duration = end_time - start_time
            print(f"{activity}: {start_time.strftime('%I:%M %p')} to {end_time.strftime('%I:%M %p')} ({duration})")
        else:
            time = convert_to_datetime(time)
            print(f"{activity}: {time.strftime('%I:%M %p')}")

# Display the routine
display_routine(routine)
