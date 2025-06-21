"""
Title: Swap Two Numbers Using a Temporary Variable
Author: Rushikesh Padaki
Date: 21 June 2025

Description:
This Python program swaps the values of two variables using a temporary variable.
- Takes input from the user for two integers.
- Demonstrates basic variable assignment and swapping logic.
- Useful for understanding data manipulation in memory.

Algorithm:
1. Read two integers from the user.
2. Print the values before swapping.
3. Use a temporary variable 'temp' to store the value of 'x'.
4. Assign the value of 'y' to 'x'.
5. Assign the value stored in 'temp' to 'y'.
6. Print the values after swapping.

Time Complexity:
- O(1) (Simple variable assignments)

Space Complexity:
- O(1) (Uses one extra temporary variable)

Sample Execution:

Case 1: User inputs x = 10, y = 20
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
"""

x = int(input('Enter the value for x: '))
y = int(input('Enter the value for y: '))

print('Values of x and y before swapping:')
print('x = ', x)
print('y = ', y)

temp = x
x = y
y = temp

print('Values of x and y after swapping:')
print('x = ', x)
print('y = ', y)
