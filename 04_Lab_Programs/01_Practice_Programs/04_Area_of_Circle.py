"""
Title: Calculate Area of a Circle
Author: Rushikesh Padaki
Date: 21 June 2025

Description:
This Python program calculates the area of a circle based on user input for the radius.
- Uses the 'math' module to access the constant value of π (pi).
- Applies the formula: Area = π × r², where r is the radius.
- Demonstrates type conversion and formatted floating-point output.

Algorithm:
1. Prompt the user to input the radius of the circle.
2. Convert the radius from string to float.
3. Use the formula 'area = π × radius²' to calculate the area.
4. Display the result using formatted output with 6 decimal places.

Time Complexity:
- O(1) (Direct calculation without loops)

Space Complexity:
- O(1) (Minimal variable usage)

Sample Execution:

Case 1: Radius = 5 cm
Input:
Enter the radius of a circle in cm: 5
Output:
The area of the circle = 78.539816 sq.cm
"""

import math

radius = input('Enter the radius of a circle in cm: ')
area = math.pi * (pow(float(radius), 2))

print('The area of the circle = %.6f sq.cm' % area)
