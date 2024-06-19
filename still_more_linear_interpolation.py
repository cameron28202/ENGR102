# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie Henderson
#               Frank Rodriguez
#               Kareem Elias
#               Cameron Stone
# Section:      501
# Assignment:   Lab 3.15
# Date:         9/7/2022
#

t1 = float(input("Enter time 1: "))
x1 = float(input("Enter the x position of the object at time 1:\n"))
y1 = float(input("Enter the y position of the object at time 1:\n"))
z1 = float(input("Enter the z position of the object at time 1:\n"))
t2 = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2:\n"))
y2 = float(input("Enter the y position of the object at time 2:\n"))
z2 = float(input("Enter the z position of the object at time 2:\n"))

x_slope = (x2-x1)/(t2-t1)
y_slope = (y2-y1)/(t2-t1)
z_slope = (z2-z1)/(t2-t1)


#hello
time = t1
for i in range(5):
    
    x_pos = x_slope * (time-t1) + x1
    y_pos = y_slope * (time-t1) + y1
    z_pos = z_slope * (time-t1) + z1
    print(f'At time {time:.2f} seconds the object is at ({x_pos:.3f}, {y_pos:.3f}, {z_pos:.3f})')
    time += (t2-t1)/4
    
    
    
    