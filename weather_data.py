# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 11.13
# Date:         11/13/2022



months= {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
    }

    

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


month = input("Please enter a month: \n")
year = int(input("Please enter a year: \n"))


max_temps = 0
num_temps = 0

wind_speeds = 0
num_wind_speeds = 0

num_precip_days = 0

#weather_list = ['hello,goodbye,hello', '1/2/2019,9.4,0,48,55,42', '1/2/2019,10,0,50,56,42', '1/2/2019,20,0,50,25,42', '1/2/2019,30,0,50,21,42', '1/2/2019,40,0,50,21,42']
for x in range(len(weather_list)):
    if x != 0:
        
        data = weather_list[x].split(",")
        date = data[0]
        nums = date.split("/")
        if int(nums[0]) == months[month] and int(nums[2]) == year:
            max_temps += int(data[4])
            num_temps += 1
            wind_speeds += float(data[1])
            num_wind_speeds += 1
            if float(data[2]) != 0:
                num_precip_days += 1
            

print(f'For {month} {year}:')
print(f'Mean maximum daily temperature: {max_temps/num_temps:.1f} F')
print(f'Mean daily wind speed: {wind_speeds/num_wind_speeds:.2f} mph')
print(f'Percentage of days with precipitation: {num_precip_days/num_wind_speeds * 100:.1f} %')
weather.close()