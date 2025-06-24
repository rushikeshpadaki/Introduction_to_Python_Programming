"""
Title: Employee Database Management System  
Author: Rushikesh Padaki  
Date: 24 June 2025  

Description:
This program implements a simple Employee Database using a dictionary where:
- Key: Employee ID (integer)
- Value: List containing [Employee Name, Date of Birth, Designation]

Features:
- Create multiple employees at once
- Add a new employee
- Search an employee by ID
- Delete an employee by ID
- Display all employees
- Exit the program

Algorithm:
1. Display a menu with options for employee operations
2. For each menu choice:
   - If 1: Prompt to enter details for multiple employees and store them in a dictionary
   - If 2: Prompt to add a new employee individually
   - If 3: Search for an employee using their ID using '.get()'
   - If 4: Remove an employee using '.pop()' if the ID exists
   - If 5: Display all employee records if any exist
   - If 6: Exit the loop
3. Repeat until the user exits

Time Complexity:
- Insert/Search/Delete: O(1) on average using dictionary operations

Space Complexity:
- O(n) where n is the number of employees stored

Sample Execution:

====== Employee Database ======
1. Create Employees  
2. Add New Employee  
3. Search Employee  
4. Delete Employee  
5. Display All Employees  
6. Exit  
===============================  
Enter your choice: 1  
Enter the number of employees: 2  
--- Enter details for Employee 1 ---  
Enter the Employee ID: 101  
Enter the Employee Name: John  
Enter the DOB (dd-mm-yyyy): 01-01-1990  
Enter the Designation: Manager  
Employee added successfully.  

--- Enter details for Employee 2 ---  
Enter the Employee ID: 102  
Enter the Employee Name: Alice  
Enter the DOB (dd-mm-yyyy): 05-05-1992  
Enter the Designation: Analyst  
Employee added successfully.  

====== MENU ======  
Enter your choice: 2  
Enter the Employee ID: 103  
Enter the Employee Name: Steve  
Enter the DOB (dd-mm-yyyy): 11-11-1995  
Enter the Designation: Engineer  
Employee added successfully.  

====== MENU ======  
Enter your choice: 3  
Enter the Employee ID to search: 101  
Employee Found: ID 101, Details: ['John', '01-01-1990', 'Manager']  

====== MENU ======  
Enter your choice: 4  
Enter the Employee ID to delete: 102  
Employee deleted successfully.  

====== MENU ======  
Enter your choice: 5  
Current Employee Database:  
ID: 101 -> Name: John, DOB: 01-01-1990, Designation: Manager  
ID: 103 -> Name: Steve, DOB: 11-11-1995, Designation: Engineer  

====== MENU ======  
Enter your choice: 6  
Exiting...
"""

# Initialize the employee dictionary
Employee = dict()

# Infinite loop to display the menu until the user exits
while True:
    # Display menu
    print('\n====== Employee Database ======\n')
    print('1. Create Employees')
    print('2. Add New Employee')
    print('3. Search Employee')
    print('4. Delete Employee')
    print('5. Display All Employees')
    print('6. Exit')
    print('===============================\n')

    # Get user choice
    Choice = int(input('Enter your choice: '))

    # Option 1: Create multiple employees
    if Choice == 1:
        n = int(input('Enter the number of employees: '))
        for i in range(n):
            print('--------------------------------')
            print(f'Enter details for Employee {i + 1}')
            print('--------------------------------')
            EmpId = int(input('Enter the Employee ID: '))
            EmpDetails = []
            EmpName = input('Enter the Employee Name: ')
            EmpDOB = input('Enter the DOB (dd-mm-yyyy): ')
            Designation = input('Enter the Designation: ')
            EmpDetails.extend([EmpName, EmpDOB, Designation])
            Employee[EmpId] = EmpDetails
            print('Employee added successfully.\n')

    # Option 2: Add a single new employee
    elif Choice == 2:
        EmpId = int(input('Enter the Employee ID: '))
        EmpDetails = []
        EmpName = input('Enter the Employee Name: ')
        EmpDOB = input('Enter the DOB (dd-mm-yyyy): ')
        Designation = input('Enter the Designation: ')
        EmpDetails.extend([EmpName, EmpDOB, Designation])
        Employee[EmpId] = EmpDetails
        print('Employee added successfully.\n')

    # Option 3: Search for an employee by ID
    elif Choice == 3:
        EId = int(input('Enter the Employee ID to search: '))
        emp = Employee.get(EId)
        if emp:
            print('--------------------------------')
            print(f'Employee Found: ID {EId}, Details: {emp}')
            print('--------------------------------')
        else:
            print('Employee not found!')

    # Option 4: Delete an employee by ID
    elif Choice == 4:
        EId = int(input('Enter the Employee ID to delete: '))
        if EId in Employee:
            Employee.pop(EId)
            print('Employee deleted successfully.')
        else:
            print('Employee ID not found.')

    # Option 5: Display all employee records
    elif Choice == 5:
        if not Employee:
            print('\nNo employee details found.\n')
        else:
            print('\nCurrent Employee Database:')
            for key, value in Employee.items():
                print(f'ID: {key} -> Name: {value[0]}, DOB: {value[1]}, Designation: {value[2]}')

    # Option 6: Exit the program
    elif Choice == 6:
        print('Exiting...')
        break

    # Handle invalid choice
    else:
        print('Invalid choice! Please select a valid option (1-6).')
