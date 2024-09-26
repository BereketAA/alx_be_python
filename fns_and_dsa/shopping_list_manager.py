def display_menu():
    """Displays the main menu options."""
    print(f"\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def add_item(shopping_list):
    """Prompts the user to add an item to the shopping list."""
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("No item entered. Please try again.")


def remove_item(shopping_list):
    """Prompts the user to remove an item from the shopping list."""
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' is not in your shopping list.")


def view_shopping_list(shopping_list):
    """Displays the current shopping list."""
    if shopping_list:
        print("\nShopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("\nYour shopping list is empty.")


def main():
    """Main function that manages the shopping list."""
    # Initialize an empty shopping list
    shopping_list = []

    while True:
        display_menu()  # Show the menu
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(shopping_list)  # Call the function to add an item
        elif choice == '2':
            remove_item(shopping_list)  # Call the function to remove an item
        elif choice == '3':
            view_shopping_list(shopping_list)  # Call the function to view the list
        elif choice == '4':
            print("Goodbye!")  # Exit message
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input


if __name__ == "__main__":
    main()