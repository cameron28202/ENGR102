# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie Henderson
#               Frank Rodriguez
#               Kareem Elias
#               Cameron Stone
# Section:      401
# Assignment:   Lab 4.15
# Date:         9/28/2022
#

from math import *

####### Part A: Variables #######

# Input variables: 
#   - len_side = the length of the side of the
#     equilaterial triangle. 
#
#   - num_layers = the number of layers in the temple

len_side = float(input("Enter the side length in meters: \n"))
num_layers = int(input("Enter the number of layers: \n"))


# Triangle_faces = the number of triangle faces we are taking
# the area of. 1, 3, 5, 7... etc
triangle_faces = 1

# square_faces = the number of square faces we are taking 
# the area of. 3, 6, 9... etc
square_faces = 3

# Area = the total area of gold covering the triangular prisms, which
# is added on to each iteration of the loop.
area = 0


####### Part B: Calculations #######
for i in range(num_layers):
    
    #area of number of triangles plus area of number of squares
    area += (triangle_faces * (sqrt(3)/4 * len_side**2)) + (square_faces * len_side**2)
    
    triangle_faces += 2
    square_faces += 3
    
    
####### Part C: Printing output #######
    
print(f'You need {area:.2f} m^2 of gold foil to cover the pyramid')



