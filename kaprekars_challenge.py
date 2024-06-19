# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 7.29
# Date:         10/14/2022

#Take user input

#Add leading zeros
count = 0
num = 0
while(num <= 9999):
    while len(str(num)) != 4:
        if num == 0:
            num = 1000
        else:
            num *= 10
    
    
    #Loop through until number is 0 or 6174, do kaprekar's routine
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
        if len(str(num)) == 3:
            num *= 10
    num += 1

print(f'Kaprekar\'s routine takes {count} total iterations for all four-digit numbers ')