"""
Title: Find ASCII Value of a Character  
Author: Rushikesh Padaki  
Date: 22 June 2025  

Description:
This program finds and displays the ASCII value of a given character.
- Takes a single character input from the user.
- Uses the built-in 'ord()' function to get its ASCII value.
- Displays the ASCII value with appropriate formatting.

Algorithm:
1. Prompt the user to enter a single character.
2. Use the 'ord()' function to get the ASCII value of the character.
3. Display the result in a formatted string.

Time Complexity:
- O(1)

Space Complexity:
- O(1)

Sample Execution:

Case 1: Alphabet character
Input:
Enter a character: A  
Output:
The ASCII value of the character "A" is  65  

Case 2: Special character
Input:
Enter a character: @  
Output:
The ASCII value of the character "@" is  64  
"""

character = input('Enter a character: ')
print('The ASCII value of the character "' + character + '" is ', ord(character))
