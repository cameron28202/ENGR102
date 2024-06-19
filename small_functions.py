# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 7.29
# Date:         10/14/2022

from math import *

def parta(r1, r2):
    #use equation
    return ((4*pi) / 3) * (r1**2 - r2**2)**(3/2)

def partb(num):
    odd_list = []
    list = []
    
    #2 lists, append odd list and define temp & ind
    for x in range(1, num, 2):
        odd_list.append(x)
    for x in range(1, len(odd_list)):
        temp = 0
        ind =x
        
        #loop thru until temp is equal to num or greater
        while (temp <= num):
            temp += odd_list[x-1]
            if temp == num:
                count = 0
                while count != num:
                    list.append(odd_list[x-1])
                    count += odd_list[x - 1]
                    x-=1
                list.sort()
                return list
            x += 1
        x = ind
    return False

print(partb(24))
    
def partc(char, name, company, email):
    
    num_chars = -1
    lengths = [len(char), len(name), len(company), len(email)]
    for x in lengths:
        if x > num_chars:
            num_chars = x
    
    #create ans string
    ans = ""
    ans += char * (num_chars + 6) + "\n"
    ans += char + " " + " " * ((num_chars - len(name) + 2) // 2) + name + " " * ((num_chars - len(name) + 2) // 2) + " "
    
    if num_chars % 2 == 0:
        ans += " "
    
    ans += char + "\n"
    ans += char + " " + " " * ((num_chars - len(company) + 2) // 2) + company + " " * ((num_chars - len(company) + 2) // 2) + " " + char +"\n"
    ans += char + " " + " " * ((num_chars - len(email) + 2) // 2) + email + " " * ((num_chars - len(email) + 2) // 2) + " " + char + "\n"
    ans += char * (num_chars + 6) + "\n"
    return ans
    

def partd(list):
    
    list.sort()
    #jello
    
    if len(list) % 2 == 0:
        median = (list[len(list)//2] + list[len(list)//2 - 1]) / 2
    else:
        median = list[len(list) // 2]
    
    ans = (min(list), median, max(list))
    return ans





def parte(times, distances):
    
    #hello
    ans = []
    for x in range(len(times)):
        if x != 0:
            change_dist = distances[x] - distances[x-1] 
            change_time = times[x] - times[x-1]
            ans += [change_dist / change_time]
        
    return ans


def partf(nums):
    
    
    #double for loop to see if each index plus another equals 2026
    for i in range(len(nums)):
        for x in range(len(nums)):
            if nums[i] + nums[x] == 2026:
                return nums[i] * nums[x]
    return False
    







