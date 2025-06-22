"""
Title: Swap Two Numbers Using Tuple Assignment  
Author: Rushikesh Padaki  
Date: 22 June 2025  

Description:
This program swaps the values of two variables using tuple unpacking in Python.
- Takes two integer inputs from the user.
- Displays the values before and after swapping using a single-line tuple assignment.

Algorithm:
1. Prompt the user to enter two integer values (x and y).
2. Display the values before swapping.
3. Swap the values using tuple unpacking: x, y = y, x.
4. Display the values after swapping.

Time Complexity:
- O(1)

Space Complexity:
- O(1)

Sample Execution:

Case 1: Swapping two different numbers
Input:
Enter the value for x: 10  
Enter the value for y: 20  
Output:
Values of x and y before swapping:  
x =  10  
y =  20  
Values of x and y after swapping:  
x =  20  
y =  10  

Case 2: Swapping equal numbers
Input:
Enter the value for x: 5  
Enter the value for y: 5  
Output:
Values of x and y before swapping:  
x =  5  
y =  5  
Values of x and y after swapping:  
x =  5  
y =  5  
"""

x = int(input('Enter the value for x: '))
y = int(input('Enter the value for y: '))

print('Values of x and y before swapping:')
print('x = ', x)
print('y = ', y)

x, y = y, x

print('Values of x and y after swapping:')
print('x = ', x)
print('y = ', y)
