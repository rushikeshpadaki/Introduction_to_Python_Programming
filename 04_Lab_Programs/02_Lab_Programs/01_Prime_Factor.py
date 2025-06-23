"""
Title: Maximum Prime Factor Finder
Author: Rushikesh Padaki
Date: 23 June 2025

Description:
This program finds the largest prime factor of a given positive integer.
- It first removes all factors of 2 from the number.
- Then it checks for odd prime factors up to the square root of the number.
- If any prime factor remains that is greater than 2, it is also considered.

Algorithm:
1. Take an integer input from the user.
2. Remove all factors of 2 and update the maximum prime factor.
3. Loop through odd numbers from 3 to sqrt(n):
   - While the number is divisible by the current factor, divide and update the maxPrime.
4. If the final number is greater than 2, it is a prime factor.
5. Print the largest prime factor found.

Time Complexity:
- O(sqrt(n)) for factor checking.

Space Complexity:
- O(1) constant space used.

Sample Execution:

Case 1: Prime factors of 13195
Input:
Enter a number: 13195
Output:
The maximum prime factor of the given number is: 29

Case 2: Prime factors of 100
Input:
Enter a number: 100
Output:
The maximum prime factor of the given number is: 5
"""

import math

n = int(input('Enter a number: '))
maxPrime = -1

# Remove all the 2s
while n % 2 == 0:
    maxPrime = 2
    n = n // 2

# Check for odd factors from 3 to sqrt(n)
for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        maxPrime = i
        n = n // i

# If n becomes a prime number greater than 2
if n > 2:
    maxPrime = n

print('The maximum prime factor of the given number is:', int(maxPrime))
