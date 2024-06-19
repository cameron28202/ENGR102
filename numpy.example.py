# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie Henderson
#               Frank Rodriguez
#               Kareem Elias
#               Cameron Stone
# Section:      401
# Assignment:   Lab 12.14
# Date:         11/16/2022
#

import numpy as np
#import matplotlib


# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)

print(A, "\n")
print(B, "\n")
print(C, "\n")

D = A.dot(B).dot(C)
print(D, "\n")

D_transpose = D.transpose()
print(D_transpose, "\n")

E = np.sqrt(D) / 2
print(E)