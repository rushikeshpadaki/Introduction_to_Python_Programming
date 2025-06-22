"""
Title: Display Calendar of a Given Month and Year  
Author: Rushikesh Padaki  
Date: 22 June 2025  

Description:
This program displays the calendar for a specific month and year using Python's built-in 'calendar' module.
- Takes year and month as input from the user.
- Uses the 'calendar.month()' function to generate the calendar.
- Prints the formatted calendar for the given month and year.

Algorithm:
1. Import the 'calendar' module.
2. Prompt the user to enter a valid year (integer).
3. Prompt the user to enter a valid month (integer from 1 to 12).
4. Call 'calendar.month(year, month)' to get the formatted string.
5. Display the calendar for the specified month and year.

Time Complexity:
- O(1)

Space Complexity:
- O(1)

Sample Execution:

Case 1: February of a leap year
Input:
Enter year: 2024  
Enter month: 2  
Output:
The calendar for the specified month and year:  
   February 2024  
Mo Tu We Th Fr Sa Su  
         1  2  3  4  
 5  6  7  8  9 10 11  
12 13 14 15 16 17 18  
19 20 21 22 23 24 25  
26 27 28 29  

Case 2: November
Input:
Enter year: 2025  
Enter month: 11  
Output:
The calendar for the specified month and year:  
   November 2025  
Mo Tu We Th Fr Sa Su  
                   1  
 3  4  5  6  7  8  9  
10 11 12 13 14 15 16  
17 18 19 20 21 22 23  
24 25 26 27 28 29 30  
"""

import calendar

YEAR = int(input("Enter year: "))
MONTH = int(input("Enter month: "))

print("The calendar for the specified month and year:")
print(calendar.month(YEAR, MONTH))
