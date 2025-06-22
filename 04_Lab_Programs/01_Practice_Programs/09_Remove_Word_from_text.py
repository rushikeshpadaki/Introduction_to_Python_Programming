"""
Title: Remove a Word from a Text  
Author: Rushikesh Padaki  
Date: 22 June 2025  

Description:
This program removes all occurrences of a specified word from the input text.
- Takes a string of text input from the user.
- Prompts the user to enter a word that needs to be removed from the text.
- Uses the 'replace()' method to remove all instances of the specified word.
- Displays the updated text after removal.

Algorithm:
1. Prompt the user to enter a line of text.
2. Prompt the user to enter the word to be removed.
3. Use the 'replace()' function to replace all instances of the word with an empty string.
4. Display the updated text.

Time Complexity:
- O(n), where n is the length of the text

Space Complexity:
- O(n), for storing the updated text

Sample Execution:

Case 1: Removing a common word
Input:
Enter some text: the quick brown fox jumps over the lazy dog  
Enter a word from text to be removed: the  
Output:
Updated Text:   quick brown fox jumps over  lazy dog  

Case 2: Removing a word not present
Input:
Enter some text: hello world  
Enter a word from text to be removed: python  
Output:
Updated Text:  hello world  
"""

text = input('Enter some text: ')

word = input('Enter a word from text to be removed: ')

text = text.replace(word, "")

print('Updated Text: ', text)
