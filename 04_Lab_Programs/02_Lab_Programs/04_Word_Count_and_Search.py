"""
Title: Word Count and Word Search in a Paragraph  
Author: Rushikesh Padaki  
Date: 24 June 2025  

Description:
This program analyzes a given paragraph to perform the following:
- Count the total number of words in the paragraph
- Calculate and display the frequency of each word
- Allow the user to search for a word and indicate whether it is found in the paragraph

Algorithm:
1. Define a multi-line string as the paragraph
2. Print the paragraph and count the total words using 'split()'
3. Initialize an empty dictionary to store word frequencies
4. Iterate through the list of words and update the dictionary accordingly
5. Display each word along with its frequency
6. Prompt the user to enter a word to search in the paragraph
7. Use 'find()' method to locate the word and display appropriate message

Time Complexity:
- O(n) where n is the number of words in the paragraph

Space Complexity:
- O(u) where u is the number of unique words in the paragraph

Sample Execution:

Entered Paragraph: New Delhi is the capital of India .
Bangalore is the captial of Karnataka . Karnataka is in India .
India is the largest democratic country in the world .
Total number of words in the paragraph: 27
Word - New, Frequency - 1
Word - Delhi, Frequency - 1
Word - is, Frequency - 4
Word - the, Frequency - 3
Word - capital, Frequency - 1
Word - of, Frequency - 2
Word - India, Frequency - 3
Word - ., Frequency - 3
Word - Bangalore, Frequency - 1
Word - captial, Frequency - 1
Word - Karnataka, Frequency - 2
Word - in, Frequency - 2
Word - largest, Frequency - 1
Word - democratic, Frequency - 1
Word - country, Frequency - 1
Word - world, Frequency - 1
Enter a word to be searched in paragraph: India
The word "India" is found in the paragraph!
"""

# Define the paragraph
paragraph = '''New Delhi is the capital of India .
Bangalore is the captial of Karnataka . Karnataka is in India .
India is the largest democratic country in the world .'''

# Display the paragraph
print('Entered Paragraph: ' + paragraph)

# Count total number of words using split()
wordCount = len(paragraph.split())
print("Total number of words in the paragraph: ", wordCount)

# Initialize an empty dictionary to hold word frequencies
counts = dict()

# Split the paragraph into words
words = paragraph.split()

# Loop through each word and update its count in the dictionary
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

# Display each word and its frequency
for word in counts:
    print('Word - ' + word + ', Frequency - ' + str(counts[word]))

# Ask user to enter a word to search
searchWord = input('Enter a word to be searched in paragraph: ')

# Use find() to check if the word exists in the paragraph
result = paragraph.find(searchWord)

# Display appropriate message based on result
if result != -1:
    print('The word "' + searchWord + '" is found in the paragraph!')
else:
    print('The word "' + searchWord + '" is not found in the paragraph!')
