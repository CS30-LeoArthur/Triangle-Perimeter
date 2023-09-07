# Triangle Perimeter
import math

print("WELCOME TO THE TRIANGLE PERIMETER PROGRAM \nEnter the coordinates of the vertices of a triangle")

# Get vertex A
print("\nVERTEX A")
x_Point_A = float(input("Enter x-coordinate for Vertex A: "))
y_Point_A = float(input("Enter y-coordinate for Vertex A: "))

# Get Vertex B
print("\nVERTEX B")
x_Point_B = float(input("Enter x-coordinate for Vertex B: "))
y_Point_B = float(input("Enter y-coordinate for Vertex B: "))

# Get Vertex C
print("\nVERTEX C")
x_Point_C = float(input("Enter x-coordinate for Vertex C: "))
y_Point_C = float(input("Enter y-coordinate for Vertex C: "))

# Calculations
side_AB = math.sqrt((x_Point_B - x_Point_A)**2 + (y_Point_B - y_Point_A)**2)
side_AC = math.sqrt((x_Point_C - x_Point_A)**2 + (y_Point_C - y_Point_A)**2)
side_BC = math.sqrt((x_Point_C - x_Point_B)**2 + (y_Point_C - y_Point_B)**2)
perimeter = side_AB + side_AC + side_BC

# Results
print ("SIDE LENGTHS & PERIMETER:")

# Side Length AB
print("AB = " + str(side_AB))

# Side Length AC
print("AC = " + str(side_AC))

# Side Length BC
print("BC = " + str(side_BC))

# Perimeter
print ("Perimeter = " + str(perimeter))