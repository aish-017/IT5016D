from datetime import datetime, timedelta

# Define the routine as a list of tuples with activity and estimated time
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
    return datetime.strptime(time_str, "%I:%M %p" # Convert time string to daytime object

# Function to display the routine
def display_routine(routine):
    for activity, time in routine: # Iterate each activity and time in routine
        if '-' in time: # Check if the time range includes a start and end time
            start_time, end_time = time.split(' - ') # Plit the time range into start and end times
            start_time = convert_to_datetime(start_time) # Convert start time to datetime object
            end_time = convert_to_datetime(end_time) # Convert end time to datetime obeject
            duration = end_time - start_time # Calculate duration of activity 
            print(f"{activity}: {start_time.strftime('%I:%M %p')} to {end_time.strftime('%I:%M %p')} ({duration})") # Print activity with start time, end time and duration 
        else:
            time = convert_to_datetime(time) # Convert single time to daytime object
            print(f"{activity}: {time.strftime('%I:%M %p')}") # Print the activity with time

# Display the routine
display_routine(routine) # call the function to display routine
