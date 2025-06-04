# Title: Swap Two Numbers Using a Temporary Variable
# Author: Rushikesh Padaki
# Date: 04 June 2025
#
# Description:
# A Python program to swap the values of two variables using a temporary variable.
# - Demonstrates the use of a third (temporary) variable to facilitate swapping.
# - Takes input from the user for the values of x and y.
# - Outputs values before and after the swap operation.
#
# Algorithm:
# 1. Prompt the user to enter values for x and y.
# 2. Store the value of x in a temporary variable 'temp'.
# 3. Assign the value of y to x.
# 4. Assign the value stored in 'temp' to y.
# 5. Print the values before and after swapping.
#
# Time Complexity:
# - O(1) — Simple assignment operations.
#
# Space Complexity:
# - O(1) — Extra space used for one temporary variable.
#
# Sample Execution:
#
# Case 1: Swap values of 10 and 20
# Input:
# Enter the value of x: 10
# Enter the value of y: 20
# Output:
# Before swapping:
# x =  10
# y =  20
# After swapping:
# x =  20
# y =  10

x = int(input('Enter the value of x: '))
y = int(input('Enter the value of y: '))

print('Before swapping:')
print('x = ', x)
print('y = ', y)

temp = x
x = y
y = temp

print('After swapping:')
print('x = ', x)
print('y = ', y)
