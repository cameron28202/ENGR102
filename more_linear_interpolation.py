# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 2.10
# Date:         8/24/2022


t1 = 12
x1 = 8
y1 = 6
z1 = 7

t2 = 85
x2 = -5
y2 = 30
z2 = 9

#calculating slope for x, y and z values
x_slope = (x2-x1)/(t2-t1)
y_slope = (y2-y1)/(t2-t1)
z_slope = (z2-z1)/(t2-t1)


for i in range(5):
    t = 30 + i * 7.5
    
    x_pos = x_slope * (t-t1) + x1
    x_str = "x" + str(i+1) +" ="
    print("At time", t, "seconds:")
    print(x_str, x_pos, "m")
    
    y_pos = y_slope * (t-t1) + y1
    y_str = "y" + str(i+1)+" ="
    print(y_str, y_pos, "m")
    
    z_pos = z_slope * (t-t1) + z1
    z_str = "z" + str(i+1)+" ="
    print(z_str, z_pos, "m")
    
    if i != 4:
        print("-----------------------")
    

