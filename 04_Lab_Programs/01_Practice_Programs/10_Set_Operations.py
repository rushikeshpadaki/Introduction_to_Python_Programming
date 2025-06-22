"""
Title: Set Operations in Python  
Author: Rushikesh Padaki  
Date: 22 June 2025  

Description:
This program performs basic set operations (union, intersection, difference, and symmetric difference) on two sets of integers.
- Defines two sets: E (even numbers) and N (natural numbers).
- Computes and displays:
  - Union of E and N
  - Intersection of E and N
  - Difference of E and N (elements in E but not in N)
  - Symmetric Difference of E and N (elements in E or N but not both)

Algorithm:
1. Define two sets E and N.
2. Use `|` operator to find the union of E and N.
3. Use `&` operator to find the intersection of E and N.
4. Use `-` operator to find the difference of E and N.
5. Use `^` operator to find the symmetric difference of E and N.
6. Print each result.

Time Complexity:
- O(n), where n is the size of the larger set

Space Complexity:
- O(n), for storing intermediate results

Sample Execution:

Case 1: Performing all four operations
Output:
Union of E and N is:  {0, 1, 2, 3, 4, 5, 6, 8}  
Intersection of E and N is:  {2, 4}  
Difference of E and N is:  {0, 6, 8}  
Symmetric Difference of E and N is:  {0, 1, 3, 5, 6, 8}  
"""

E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

print("Union of E and N is: ", E | N)
print("Intersection of E and N is: ", E & N)
print("Difference of E and N is: ", E - N)
print("Symmetric Difference of E and N is: ", E ^ N)
