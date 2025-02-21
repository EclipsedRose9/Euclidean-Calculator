# My solution for our question uses an input method to calculate value's in a format (x,y) adhering to the
# Cartesian coordinate system to determine the two with the highest difference in distance and print it out

import math
# Lines 7-13 is a loop method to get three points from the user in the correct format
points = []  # This creates an empty list that store's the user points
for i in range(3):  # This is the prompt for user to enter the coordinates of each point
    while True:  # Loop to prevent input error, must adhere to the correct format
        point = input(f"Enter point {i+1} in the format x,y: ")  # User input prompt
        try:  # handle's user input error's
            x, y = map(float, point.split(","))  #
            points.append((x, y))
            break  # breaks out of the while loop if the correct format is inputted
        except:  # if the while loop doesn't break an error message is print
            print("Please try again in the format: x,y")

# Lines 19-28 uses a formula to find out of the three user inputs which two are the furthest apart
max_distance = 0  # This variable is created to keep track of any two points to find the max distance
point1 = None  # Variables to keep track of the two points that are the furthest apart
point2 = None
for i in range(len(points)):  # Range function triggers a loop to calculate the distance between every possible point's input
    for j in range(i+1, len(points)):
        distance = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
        #  Calculates the Euclidean distance between i and j using pythagoras theorem
        if distance > max_distance:
            max_distance = distance  # updates the variable
            point1 = points[i]
            point2 = points[j]

# Calculate the difference in distance between coordinates of the two points
x_distance = point2[0] - point1[0]
y_distance = point2[1] - point1[1]

# Format the x and y distances with the correct symbol (+ or -) based on user inputs
x_str = f"x = {'+' if x_distance >= 0 else ''}{x_distance:.2f}"
y_str = f"y = {'+' if y_distance >= 0 else ''}{y_distance:.2f}"

# Print the results
print(f"The two points which are farthest apart are {point1} and {point2}")
print(f"The distance being {x_str} and {y_str}.")


