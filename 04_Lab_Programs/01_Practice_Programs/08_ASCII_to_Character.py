"""
Title: Find Character from ASCII Value  
Author: Rushikesh Padaki  
Date: 22 June 2025  

Description:
This program finds and displays the character corresponding to a given ASCII value.
- Takes an integer input representing a valid ASCII code.
- Uses the built-in 'chr()' function to convert it to the corresponding character.
- Displays the character using formatted output.

Algorithm:
1. Prompt the user to enter a valid ASCII value (integer between 0 and 127 for standard ASCII).
2. Use the 'chr()' function to convert the value to a character.
3. Display the resulting character with appropriate formatting.

Time Complexity:
- O(1)

Space Complexity:
- O(1)

Sample Execution:

Case 1: Uppercase letter
Input:
Enter a valid ASCII value: 66  
Output:
The character associated with the ASCII value "66" is  B  

Case 2: Special symbol
Input:
Enter a valid ASCII value: 36  
Output:
The character associated with the ASCII value "36" is  $  
"""

ascii_value = int(input('Enter a valid ASCII value: '))
print('The character associated with the ASCII value "' + str(ascii_value) + '" is ', chr(ascii_value))
