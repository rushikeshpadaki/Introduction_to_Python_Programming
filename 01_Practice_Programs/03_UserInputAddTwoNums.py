# Title: Addition of Two Numbers with User Input
# Author: Rushikesh Padaki
# Date: 04 June 2025
#
# Description:
# A Python program to accept two numbers as input from the user, compute their sum, and display the result.
# - Uses the input() function to get values from the user.
# - Converts input strings to floating-point numbers using float().
# - Uses the format() method to display a formatted output message.
#
# Algorithm:
# 1. Prompt the user to enter the first number and store it in 'num1'.
# 2. Prompt the user to enter the second number and store it in 'num2'.
# 3. Convert both inputs to float type.
# 4. Compute the sum and store in 'total'.
# 5. Print the formatted result using the format() method.
#
# Time Complexity:
# - O(1) — Basic input/output and arithmetic operations.
#
# Space Complexity:
# - O(1) — Constant space for three variables.
#
# Sample Execution:
#
# Case 1: Valid floating-point inputs
# Input:
# Enter first number: 3.2
# Enter second number: 4.8
# Output:
# The sum of 3.2 and 4.8 is 8.0

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

total = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, total))
