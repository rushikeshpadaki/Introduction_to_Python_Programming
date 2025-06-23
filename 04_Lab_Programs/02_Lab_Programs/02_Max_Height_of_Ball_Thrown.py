"""
Title: Maximum Height of a Vertically Thrown Ball
Author: Rushikesh Padaki
Date: 23 June 2025

Description:
This program calculates the maximum height reached by a ball thrown vertically upwards from a player's hand.
- Uses initial velocity and height of the player.
- Applies standard kinematic equations:
  - Time to reach maximum height: t = -initial_velocity / acceleration_due_to_gravity
  - Maximum height above hand: height = initial_velocity * time + 0.5 * acceleration * time^2
  - Total height from ground = player's height + ball height above hand

Algorithm:
1. Read initial velocity and player's height from user.
2. Define acceleration due to gravity as -9.8 m/s².
3. Calculate time to reach maximum height.
4. Calculate maximum height above player's hand.
5. Calculate total height from the ground.
6. Display all results.

Time Complexity:
- O(1) constant time calculations.

Space Complexity:
- O(1) constant space used.

Sample Execution:

Case 1:
Input:
Enter the velocity of the ball in m/s: 15
Enter the height of the player in meters: 1.75
Output:
Time taken by ball to reach maximum height in seconds:  1.53
Height reached by ball in meters:  11.47
Total height reached by ball from ground in meters:  13.22
"""

# Acceleration due to gravity (in m/s^2)
acceleration_due_to_gravity = -9.8

# Input initial velocity of the ball in m/s
initial_velocity = float(input('Enter the velocity of the ball in m/s: '))

# Input player's height in meters
player_height = float(input('Enter the height of the player in meters: '))

# Calculate time to reach maximum height (when final velocity is 0)
time_to_max_height = -initial_velocity / acceleration_due_to_gravity
print('Time taken by ball to reach maximum height in seconds: ', round(time_to_max_height, 2))

# Calculate height above the player's hand
height_above_hand = (initial_velocity * time_to_max_height) + (0.5 * acceleration_due_to_gravity * (time_to_max_height ** 2))
print('Height reached by ball in meters: ', round(height_above_hand, 2))

# Calculate total height from ground
total_height = height_above_hand + player_height
print('Total height reached by ball from ground in meters: ', round(total_height, 2))
