"""
Title: Fibonacci Series and Golden Ratio Approximation
Author: Rushikesh Padaki
Date: 23 June 2025

Description:
This program generates the Fibonacci series up to a user-specified number of terms (n ≥ 2) and calculates the approximate values of the Golden Ratio.
- The Fibonacci sequence is generated using the recurrence relation: F(n) = F(n-1) + F(n-2)
- The Golden Ratio is approximated by: F(n) / F(n-1) for n ≥ 2

Algorithm:
1. Prompt the user to enter a value of n ≥ 2.
2. Initialize the Fibonacci series with the first two terms: [0, 1].
3. Generate remaining Fibonacci terms up to n.
4. For each term from index 2 onward, compute the golden ratio approximation.
5. Display the generated Fibonacci series and golden ratio values.

Time Complexity:
- O(n) for generating Fibonacci terms and golden ratios.

Space Complexity:
- O(n) for storing the Fibonacci list and golden ratios.

Sample Execution:

Case 1:
Input:
Enter the number of terms to be generated in Fibonacci Series (n ≥ 2): 6
Output:
Fibonacci Series:  [0, 1, 1, 2, 3, 5]
Golden Ratio:  [1.0, 2.0, 1.5, 1.6666666666666667]

Case 2:
Input:
Enter the number of terms to be generated in Fibonacci Series (n ≥ 2): 8
Output:
Fibonacci Series:  [0, 1, 1, 2, 3, 5, 8, 13]
Golden Ratio:  [1.0, 2.0, 1.5, 1.6666666666666667, 1.6, 1.625]
"""

# Input from user
n = int(input('Enter the number of terms to be generated in Fibonacci Series (n ≥ 2): '))

# Ensure n is at least 2
if n < 2:
    print('Invalid input. Please enter a value of n ≥ 2.')
else:
    # Initialize Fibonacci series
    fibonacci_series = [0, 1]

    # Generate remaining terms
    for i in range(2, n):
        fibonacci_series.append(fibonacci_series[i - 1] + fibonacci_series[i - 2])

    print('Fibonacci Series: ', fibonacci_series)

    # Calculate Golden Ratio values
    golden_ratios = [fibonacci_series[i] / fibonacci_series[i - 1] for i in range(2, n)]
    print('Golden Ratio: ', golden_ratios)
