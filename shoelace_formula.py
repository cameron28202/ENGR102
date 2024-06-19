# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 7.29
# Date:         10/26/2022


#getpoints method
def getpoints(arg):
    split = arg.split()
    ans = []
    for x in split:
        nums = x.split(",")
        ans.append([int(nums[0]), int(nums[1])])
    return ans
        
#cross method
def cross(list1, list2):
    return (list1[0] * list2[1]) - (list1[1] * list2[0])

#shoelace method
def shoelace(points):
    points.append(points[0])

    ans = 0
    for x in range(len(points) - 1):
        ans += cross(points[x], points[x+1])
    return ans / 2

#main method
def main():
    inp = input("Please enter the vertices:\n")
    points = getpoints(inp)
    
    print(f'The area of the polygon is {shoelace(points)}')



if __name__ == '__main__':
    main() 
 