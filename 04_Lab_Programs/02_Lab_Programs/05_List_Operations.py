"""
Title: List Operations using Menu-driven Program  
Author: Rushikesh Padaki  
Date: 24 June 2025  

Description:
This program performs various operations on a list of integers using a menu-driven approach:
- Creates an initial list from user input
- Allows insertion at a specific index
- Allows deletion of an element from a specific index
- Allows appending an element at the end
- Displays the contents of the list
- Allows graceful exit from the loop

Algorithm:
1. Take input for the initial size of the list and populate the list
2. Display a menu with options for insert, delete, append, display, and exit
3. Perform corresponding operations based on user input using:
   - 'insert(index, value)'
   - 'pop(index)'
   - 'append(value)'
   - 'print()'
4. Loop continues until user selects Exit

Time Complexity:
- Insert: O(n)
- Delete: O(n)
- Append: O(1)
- Display: O(n)

Space Complexity:
- O(n), where n is the number of elements in the list

Sample Execution:

Enter the size of the list: 3  
Enter an element to be inserted: 10  
Enter an element to be inserted: 20  
Enter an element to be inserted: 30  
Initial List:  [10, 20, 30]  

===============MENU===============  
1. Insert at a specific position  
2. Remove an element from the list  
3. Add an element to the list  
4. Display the list  
5. Exit  
Enter your choice: 1  
Enter the position where element needs to be inserted: 1  
Enter an element to be inserted: 99  

===============MENU===============  
1. Insert at a specific position  
2. Remove an element from the list  
3. Add an element to the list  
4. Display the list  
5. Exit  
Enter your choice: 2  
Enter the position from where you want to delete an element: 0  

===============MENU===============  
1. Insert at a specific position  
2. Remove an element from the list  
3. Add an element to the list  
4. Display the list  
5. Exit  
Enter your choice: 3  
Enter an element to be added: 88  

===============MENU===============  
1. Insert at a specific position  
2. Remove an element from the list  
3. Add an element to the list  
4. Display the list  
5. Exit  
Enter your choice: 4  
List Contents:  [99, 20, 30, 88]  

===============MENU===============  
1. Insert at a specific position  
2. Remove an element from the list  
3. Add an element to the list  
4. Display the list  
5. Exit  
Enter your choice: 5  
Exiting....
"""

# Initialize an empty list
numbers = []

# Get the size of the list from user
n = int(input('Enter the size of the list: '))

# Collect 'n' elements from the user
while n > 0:
    i = int(input('Enter an element to be inserted: '))
    numbers.append(i)
    n = n - 1

# Display the initial list
print('Initial List: ', numbers)

# Infinite loop for menu-driven operations
while True:
    # Display menu options
    print('===============MENU===============')
    print('1. Insert at a specific position')
    print('2. Remove an element from the list')
    print('3. Add an element to the list')
    print('4. Display the list')
    print('5. Exit')
    
    # Read user choice
    choice = int(input('Enter your choice: '))
    
    # Insert an element at a specific index
    if choice == 1:
        position = int(input('Enter the position where element needs to be inserted: '))
        item = int(input('Enter an element to be inserted: '))
        numbers.insert(position, item)
        
    # Remove an element from a specific index
    elif choice == 2:
        position = int(input('Enter the position from where you want to delete an element: '))
        numbers.pop(position)
        
    # Append an element to the end of the list
    elif choice == 3:
        item = int(input('Enter an element to be added: '))
        numbers.append(item)
        
    # Display current contents of the list
    elif choice == 4:
        print('List Contents: ', numbers)
        
    # Exit the loop and end the program
    elif choice == 5:
        print('Exiting....')
        break
    
    # Handle invalid menu option
    else:
        print('Invalid Choice!!!')
