tasks = [] #create an empty list to store tasks.

# Function to display options.
def display_menu():
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Quit")

# Function to add a task to the list. 
def add_task():
    new_task = input("Enter a New Task: ") # Prompt user to enter a new task. 
    tasks.append(new_task) # Add task to the list.
    print(f"Task {new_task} added successfully.")
    

# Function to view all tasks in the list.
def view_task():
    global tasks
    if not tasks:
        print("No tasks to show.")
        return
    print("\nTask List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print() # Print a blank line for better readability.
  
# Function to delete a task from the list.
def delete_task():
    global tasks
    if not tasks:
        print("No tasks to delete.")
        return
    
    while True:
        print("\nTask List:") # Display the current list of tasks.
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
# Prompt the user for which task they want to delete. Cast the type to 'integer'. Input() returns a string by default. 
        try:
            choice = int(input("Which task do you want to delete?"))
            choice = (choice - 1) # Reduce the value of their input by 1 to give us a proper index number
            tasks.pop(choice) # Remove the desired element from the list
            print("Task deleted successfully.")
            print(tasks)
            break

        except ValueError:
            print("Invalid Entry.Enter a valid number")
        except IndexError:
            print("That number is not a list item. Choice a number from the list above.")        
    
# Main function (start of the program).
def main():
        # Infinite Loop
        while True: 
            display_menu()
            choice = input("What would you like to do?: ").strip()

            if choice == "1":
                add_task()
            elif choice == "2":
                view_task()
            elif choice == "3":
                delete_task()
            elif choice == "4":
                break
            else: 
                print("Invalid choice. Please try again.")

              


main() # starts your program.  