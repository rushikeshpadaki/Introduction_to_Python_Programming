"""
Title: Menu-Driven Set and Tuple Operations  
Author: Rushikesh Padaki  
Date: 24 June 2025  

Description:
This program provides a menu-based interface for performing various operations on sets and tuples:
- For Sets: Add, Remove, Update, Display elements
- For Tuples: Append elements, Delete entire tuple, Display contents

Algorithm:
1. Initialize an empty set and an empty tuple
2. Use an infinite loop to show main menu: 'S' for Set, 'T' for Tuple, 'N' to Terminate
3. For Set:
   - Option 1: Add single element using 'add()'
   - Option 2: Remove an element using 'discard()'
   - Option 3: Add multiple elements using 'update()'
   - Option 4: Display set
4. For Tuple:
   - Option 1: Add element (using tuple concatenation)
   - Option 2: Delete the tuple by reinitializing to empty
   - Option 3: Display the tuple
5. Repeat until user selects 'N' to terminate the program

Time Complexity:
- Set Operations:
  - Add/Remove/Update: O(1) average
- Tuple Operations:
  - Append: O(n) (due to immutability and re-creation)
  - Delete: O(1)

Space Complexity:
- O(n), where n is the number of elements stored in set or tuple

Sample Execution:

Enter your choice  
S : Set Operation  
T : Tuple Operation  
N : Terminate  
> s

Choose the Set operation  
1 : Add/Insert  
2 : Remove/Delete  
3 : Update/Append  
4 : Display/View  
0 : Exit  
Enter operation number: 1  
Enter the element to add: apple  
Updated Set: {'apple'}

Choose the Set operation  
Enter operation number: 3  
Enter multiple elements to update (comma separated): mango,banana  
Updated Set: {'banana', 'apple', 'mango'}

Enter your choice  
> t  

Choose the Tuple operation  
1 : Add/Insert  
2 : Delete Tuple  
3 : Display/View  
0 : Exit  
Enter operation number: 1  
Enter the element to add: green  
Updated Tuple: ('green',)

Enter operation number: 3  
Current Tuple: ('green',)

Enter your choice  
> n  
Program terminated.
"""

# Initialize empty set and tuple
setdata = set()
tupledata = tuple()

# Run infinite loop for main menu
while True:
    # Main menu for set or tuple operations
    choice = input("Enter your choice\nS : Set Operation\nT : Tuple Operation\nN : Terminate\n").lower()

    # ===================== Set Operations =====================
    if choice == 's':
        while True:
            print("\nChoose the Set operation")
            print("1 : Add/Insert")
            print("2 : Remove/Delete")
            print("3 : Update/Append")
            print("4 : Display/View")
            print("0 : Exit")

            operations = int(input("Enter operation number: "))

            if operations == 1:
                # Add a single element to the set
                data = input("Enter the element to add: ")
                setdata.add(data)
                print("Updated Set:", setdata)

            elif operations == 2:
                # Remove an element from the set using discard (safe)
                data = input("Enter the element to delete: ")
                setdata.discard(data)
                print("Updated Set:", setdata)

            elif operations == 3:
                # Add multiple elements (comma-separated input)
                data_list = input("Enter multiple elements to update (comma separated): ").split(',')
                setdata.update(data_list)
                print("Updated Set:", setdata)

            elif operations == 4:
                # Display current set
                print("Current Set:", setdata)

            elif operations == 0:
                # Exit set operations menu
                break

            else:
                print("Invalid Choice. Try again.")

    # ===================== Tuple Operations =====================
    elif choice == 't':
        while True:
            print("\nChoose the Tuple operation")
            print("1 : Add/Insert")
            print("2 : Delete Tuple")
            print("3 : Display/View")
            print("0 : Exit")

            operations = int(input("Enter operation number: "))

            if operations == 1:
                # Append an element by reassigning tuple
                data = input("Enter the element to add: ")
                tupledata += (data,)  # Add as a new single-element tuple
                print("Updated Tuple:", tupledata)

            elif operations == 2:
                # Delete the tuple (reinitialize)
                tupledata = ()
                print("Tuple Deleted.")

            elif operations == 3:
                # Display current tuple
                print("Current Tuple:", tupledata)

            elif operations == 0:
                # Exit tuple operations menu
                break

            else:
                print("Invalid Choice. Try again.")

    # ===================== Program Termination =====================
    elif choice == 'n':
        print("Program terminated.")
        break

    # Handle invalid choice from main menu
    else:
        print("Invalid Choice! Please enter 'S', 'T', or 'N'.")
