# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 7.27
# Date:         10/14/2022

from math import *


#Take user input
inp_a = str(input("Enter the elements for vector A: \n"))
inp_b = str(input("Enter the elements for vector B: \n"))

#Convert input into float list
temp_vector_a = inp_a.split(" ")
temp_vector_b = inp_b.split(" ")

vector_a = []
vector_b = []

for x in temp_vector_a:
    vector_a.append(float(x))
for x in temp_vector_b:
    vector_b.append(float(x))

#Vector magnitude
mag_a = 0
mag_b = 0
for i in range(len(vector_a)):
    mag_a += vector_a[i]**2
    mag_b += vector_b[i]**2
    
mag_a = sqrt(mag_a)
mag_b = sqrt(mag_b)

#Add vectors
add = []
for i in range(len(vector_a)):
    add.append(vector_a[i] + vector_b[i])

#Subtract vectors
subtract = []
for i in range(len(vector_a)):
    subtract.append(vector_a[i] - vector_b[i])
    
#Dot product of vectors
dot_product = 0
for i in range(len(vector_a)):
    dot_product += vector_a[i] * vector_b[i]



#Print to user
print(f'The magnitude of vector A is {mag_a:.5f}')
print(f'The magnitude of vector B is {mag_b:.5f}')
print(f'A + B is {add}')
print(f'A - B is {subtract}')
print(f'The dot product is {dot_product:.2f}')