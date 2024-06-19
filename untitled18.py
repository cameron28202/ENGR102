# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 11.13
# Date:         11/13/2022

weather = open("WeatherDataCLL.csv", "r")
weather_list = list(weather)
max_temp = -1
min_temp = 100
avg_precip = 0


for x in range(len(weather_list)):
    
    if x != 0:
        data = weather_list[x].split(",")
        #if the max temp for this year is greater than curr max temp, set max_temp equal to this number
        if int(data[4]) > max_temp:
            max_temp = int(data[4])
        
        #same for max temp but with minimum
        if int(data[5]) < min_temp:
            min_temp = int(data[5])
        
        #add precip from every year to the avg_precip variable to be divided by the total # of years after
        avg_precip += float(data[2])

avg_precip /= (len(weather_list) -1)
print(f'3-year maximum temperature: {max_temp} F')
print(f'3-year minimum temperature: {min_temp} F')
print(f'3-year average precipitation: {avg_precip:.3f} inches')

weather.close()