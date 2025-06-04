# Title: Area of a Circle Calculator
# Author: Rushikesh Padaki
# Date: 04 June 2025
#
# Description:
# A Python program to calculate the area of a circle based on user-provided radius.
# - Utilizes the `math` module for the value of π (pi).
# - Accepts radius as input from the user and calculates area using the formula A = π * r².
# - Displays the area with 6 decimal places using formatted string output.
#
# Algorithm:
# 1. Import the math module to access the constant pi.
# 2. Prompt the user to enter the radius of the circle.
# 3. Convert the input to a floating-point number.
# 4. Compute the area using the formula: area = π * radius².
# 5. Print the result formatted to six decimal places.
#
# Time Complexity:
# - O(1) — Single arithmetic computation and formatted print.
#
# Space Complexity:
# - O(1) — Constant space usage for radius and area variables.
#
# Sample Execution:
#
# Case 1: Circle with radius 5.0 cm
# Input:
# Enter the radius of the circle (in cm): 5.0
# Output:
# Area of the circle is: 78.539816 sq.cm

import math

radius = input('Enter the radius of the circle (in cm): ')

area = math.pi * (float(radius) ** 2)

print('Area of the circle is: %.6f sq.cm' % area)
