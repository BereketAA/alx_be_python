from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in a readable format."""
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    print(f"Current date and time: {formatted_date}")  # Print the formatted date

def calculate_future_date():
    """Calculates a future date based on user input of days."""
    days_to_add = int(input("Enter the number of days to add to the current date: "))  # Prompt user for input
    current_date = datetime.now()  # Get the current date
    future_date = current_date + timedelta(days=days_to_add)  # Calculate future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
    print(f"Future date: {formatted_future_date}")  # Print the result

def main():
    """Main function to run all demonstrations."""
    print("Exploring the datetime module:\n")
    display_current_datetime()  # Display current date and time
    calculate_future_date()  # Calculate and display future date

if __name__ == "__main__":
    main()