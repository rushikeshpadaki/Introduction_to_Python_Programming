"""
Title: Addition of Two Numbers Entered by User
Author: Rushikesh Padaki
Date: 21 June 2025

Description:
This Python program takes two numbers as input from the user, adds them, and displays the result.
- Demonstrates the use of 'input()' function for user input.
- Uses 'float()' type conversion to perform arithmetic on numeric input.
- Outputs the result using formatted string.

Algorithm:
1. Prompt the user to enter two numbers using 'input()'.
2. Convert the input strings to float using 'float()'.
3. Add the two floating-point numbers.
4. Display the result using formatted output.

Time Complexity:
- O(1) (Simple input, conversion, addition, and output)

Space Complexity:
- O(1) (Only a few variables used)

Sample Execution:

Case 1: User inputs 3.2 and 4.1
Input:
Enter first number: 3.2
Enter second number: 4.1
Output:
The sum of 3.2 and 4.1 is 7.3
"""

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

sum = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'. format(num1, num2, sum))
