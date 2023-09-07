# Triangle Perimeter
import math
def main():
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
    side_AB = dist(x_Point_A, y_Point_A, x_Point_B, y_Point_B)
    side_AC = dist(x_Point_A, y_Point_A, x_Point_C, y_Point_C)
    side_BC = dist(x_Point_B, y_Point_B, x_Point_C, y_Point_C)
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



# Distance Function
def dist(x1, y1, x2, y2):
    math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

main()
