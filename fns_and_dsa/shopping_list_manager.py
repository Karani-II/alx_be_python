def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            input_item = input("Enter the item to add: ")
            def add_item(input_item):
                shopping_list.append(input_item)
            add_item(input_item)
            print(f"Item '{input_item}' addeded to the shopping list.")

        elif choice == '2':
            remove_item = input("Remove Item:")
            def remove_item(item):
                if item in shopping_list and item:
                    shopping_list.remove(item)
                    print(f"Item '{item}' removed from the shopping list.")
                else:
                    print(f"Item '{item}' not found in the shopping list.")
                    remove_item(item)
            pass
        elif choice == '3':
            print("Current shopping list:")
            if shopping_list:
                for item in shopping_list:
                    print(f"- {item}")
                else:
                    print("shopping list is empty.")
                    pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()