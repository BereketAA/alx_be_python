# Ask the user to input a task description
task = input("Enter your task: ")

# Prompt for the task's priority (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use Match Case to react based on task priority
match priority:
    case 'high':
        priority_message = "a high priority task"
    case 'medium':
        priority_message = "a medium priority task"
    case 'low':
        priority_message = "a low priority task."
    case _:
        priority_message = "an invalid priority task"

# Modify the reminder if the task is time-bound
if time_bound == 'yes':
    time_message = "that requires immediate attention today!"
    reminder_label = "Reminder"
else:
    time_message = "Consider completing it when you have free time."
    reminder_label = "Note"

# Print the final reminder
print(f"\n{reminder_label}: '{task}' is {priority_message} {time_message}")