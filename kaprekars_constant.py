# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 7.28
# Date:         10/14/2022


#Take user input
inp = input("Enter a four-digit integer: \n")

temp = inp
#Add leading zeros
while len(inp) != 4:
    inp += "0"
    

#Define num, the answer
num = int(inp)
#Define count, number of iterations
count = 0


#Loop through until number is 0 or 6174, do kaprekar's routine
print(f'{temp} > ', end = '')
while num != 6174 and num != 0:
    
    list = []
    for i in str(num):
        list.append(i)
            
    desc_list = sorted(list, reverse = True)
    asc_list = sorted(list)
    desc = ""
    asc = ""
    
    
    for i in range(len(desc_list)):
        desc += desc_list[i]
        asc += asc_list[i]
    
    num = int(desc) - int(asc)
    count += 1
    print(f'{num} ', end = '')
    if num != 6174 and num != 0:
        print("> ", end = '')
    
    if len(str(num)) == 3:
        num *= 10

#Print output to user
print(f'\n{temp} reaches {num} via Kaprekar\'s routine in {count} iterations')