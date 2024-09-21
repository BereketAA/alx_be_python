# Ask the user for input
size = int(input("Enter the size of the  pattern: "))
# Ensure the user entered a positive integer
while size <= 0:
    print("Enter the size of the  pattern.")
    size = int(input("Enter the size of the  pattern: "))

# Use nested loops to print the square pattern
for i in range(size):
    for j in range(size):
        print("*", end=" ")  # Print * on the same line with a space
    print()  # Move to the next line after printing one row