def main():
    print("Python List Operations")
    print("1. Create a new list")
    print("2. Add elements to the list")
    print("3. Access elements from the list")
    print("4. Remove elements from the list")
    print("5. Exit")

    my_list = None

    while True:
        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                # Create a new list
                my_list = []
                print("A new list has been created.")

            elif choice == 2:
                # Add elements to the list
                if my_list is not None:
                    elements = input("Enter elements to add (comma-separated): ").split(',')
                    my_list.extend([element.strip() for element in elements])
                    print("Updated list:", my_list)
                else:
                    print("Please create a list first!")

            elif choice == 3:
                # Access elements from the list
                if my_list is not None:
                    if my_list:
                        index = int(input(f"Enter index (0 to {len(my_list) - 1}): "))
                        if 0 <= index < len(my_list):
                            print(f"Element at index {index}: {my_list[index]}")
                        else:
                            print("Index out of range.")
                    else:
                        print("The list is empty.")
                else:
                    print("Please create a list first!")

            elif choice == 4:
                # Remove elements from the list
                if my_list is not None:
                    if my_list:
                        element = input("Enter element to remove: ")
                        if element in my_list:
                            my_list.remove(element)
                            print("Updated list:", my_list)
                        else:
                            print("Element not found in the list.")
                    else:
                        print("The list is empty.")
                else:
                    print("Please create a list first!")

            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()