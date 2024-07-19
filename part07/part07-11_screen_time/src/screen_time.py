# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename: ")
starting_date = input("Starting date: ")
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
start = datetime.strptime(starting_date, "%d.%m.%Y")
to_start = start
screen_time = []
for i in range(days):
    temp = input(f"Screen time {start.strftime("%d.%m.%Y")}: ")
    screen_time.append(temp)
    to_start += timedelta(days=1)

to_start -= timedelta(days=1)

total_minutes = 0
for day in screen_time:
    temp = day.split(" ")
    for minutes in temp:
        total_minutes += int(minutes)

screen_time_formated = []
for day in screen_time:
    temp = day.replace(" ", "/")
    screen_time_formated.append(temp)

      
with open(filename, "w") as file:
    file.write(f"Time period: {start.strftime("%d.%m.%Y")}-{to_start.strftime("%d.%m.%Y")}\n")
    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {total_minutes/len(screen_time):.1f}\n")
    for i in range(days):
        file.write(f"{start.strftime("%d.%m.%Y")}: {screen_time_formated[i]}\n")
        start += timedelta(days=1)