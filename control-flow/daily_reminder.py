# Ask the user to input a task description
task = input("Enter your task:")

# Prompt for the task's priority (high, medium, low)
priority = input("Priority (high/medium/low):").lower()

# Ask if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no):").lower()

#initialize reminder

if time_bound == "yes":
    reminder = " "
else:
    reminder = " "
# Use Match Case to react based on task priority
match priority:
    case 'high':
        reminder += f"'{task}' is a high priority task"
        #reminder_label = "Reminder"
    case 'medium':
        reminder += f"'{task}' is a medium priority task"
        #reminder_label = "Reminder"
    case 'low':
        reminder += f"'{task}' is a low priority task"
        #reminder_label = "Note"
    case _:
        reminder += "invalid priority task."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += "that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

    
# Print the final reminder
#print(reminder)
print(f"Reminder:{reminder}")