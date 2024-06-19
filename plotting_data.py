# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 12.17
# Date:         11/28/2022

import matplotlib.pyplot as py
weather_file = open('WeatherDataCLL.csv', 'r')
weather_list = weather_file.readlines()
py.style.use('seaborn')

max_temp = []
min_temp = []
dates = []
wind = []
precip = []
avg_temp = []
days = []
day = 1

for x in range(len(weather_list)):
    weather_list[x] = weather_list[x][0:-1].split(',')
    weather_list[x][0] = weather_list[x][0].split('/')

for i in range(1, len(weather_list)):
    #dates index 0
    dates += [(weather_list[i][0])]
    #wind index 1
    wind += [(float(weather_list[i][1]))]
    #precipitation index 2
    precip += [(float(weather_list[i][2]))]
    #avg_temp index 3
    avg_temp += [(weather_list[i][3])]
    #max_temp index 4
    max_temp += [(int(weather_list[i][4]))]
    #min_temp index 5
    min_temp += [(int(weather_list[i][5]))]
    #add days, increment num days
    days += [(day)]
    day += 1

#red and blue line graph
fig, plot1 = py.subplots()
plot1.set_xlabel('Date')
plot1.set_ylabel('Maximum Temperature in F')
plot1.plot(days, max_temp, 'r', label = 'Maximum Temperature')
py.legend(loc = 'upper right')
plot2 = plot1.twinx()
plot2.set_ylabel('Average Wind Speed in MPH')
plot2.plot(days, wind, 'b', label = 'Avg Wind')
plot2.tick_params(axis = 'y')
py.legend(loc = 'lower left')
py.title('Max Temp and Avg Wind Speed')
py.show()



#black dot graph
py.scatter(min_temp, wind, color ='black', s = 5)
py.xlabel('Min. Temp in F')
py.ylabel('Average Wind Speed in MPH')
py.title('Average Wind Speed VS Minimum Temp.')
py.show()


#green bar graph
py.hist(wind, bins = 27, color = 'g', edgecolor = 'black')
py.xlabel('Avg. Wind Speed in MPH')
py.ylabel('Number of Days')
py.title('Histogram of Avg. Wind Speed')
py.show()



#create lists of months by number, averages, max and min
months = []
for x in range(12):
    months += [x+1]


avg_1 = []
avg_2 = []
avg_3 = []
avg_4 = []
avg_5 = []
avg_6 = []
avg_7 = []
avg_8 = []
avg_9 = []
avg_10 = []
avg_11 = []
avg_12 = []


for i in range(len(weather_list)):
    x = weather_list[i][0][0]
    
    if x == '1':
        avg_1 += [int(weather_list[i][3])]
    if x == '2':
        avg_2 += [int(weather_list[i][3])]
    if x == '3':
        avg_3 += [int(weather_list[i][3])]
    if x == '4':
        avg_4 += [int(weather_list[i][3])]
    if x == '5':
        avg_5 += [int(weather_list[i][3])]
    if x == '6':
        avg_6 += [int(weather_list[i][3])]
    if x == '7':
        avg_7 += [int(weather_list[i][3])]
    if x == '8':
        avg_8 += [int(weather_list[i][3])]
    if x == '9':
        avg_9 += [int(weather_list[i][3])]
    if x == '10':
        avg_10 += [int(weather_list[i][3])]
    if x == '11':
        avg_11 += [int(weather_list[i][3])]
    if x == '12':
        avg_12 += [int(weather_list[i][3])]
        
max_list = []
max_list += [max(avg_1)] 
max_list += [max(avg_2)]
max_list += [max(avg_3)]
max_list += [max(avg_4)] 
max_list += [max(avg_5)] 
max_list += [max(avg_6)] 
max_list += [max(avg_7)] 
max_list += [max(avg_8)] 
max_list += [max(avg_9)] 
max_list += [max(avg_10)] 
max_list += [max(avg_11)] 
max_list += [max(avg_12)] 

min_list = []
min_list += [min(avg_1)]
min_list += [min(avg_2)]
min_list += [min(avg_3)]
min_list += [min(avg_4)]
min_list += [min(avg_5)]
min_list += [min(avg_6)]
min_list += [min(avg_7)]
min_list += [min(avg_8)]
min_list += [min(avg_9)]
min_list += [min(avg_10)]
min_list += [min(avg_11)]
min_list += [min(avg_12)]

avg_list = []
avg_list += [sum(avg_1) / len(avg_1)]
avg_list += [sum(avg_2) / len(avg_2)]
avg_list += [sum(avg_3) / len(avg_3)]
avg_list += [sum(avg_4) / len(avg_4)]
avg_list += [sum(avg_5) / len(avg_5)]
avg_list += [sum(avg_6) / len(avg_6)]
avg_list += [sum(avg_7) / len(avg_7)]
avg_list += [sum(avg_8) / len(avg_8)]
avg_list += [sum(avg_9) / len(avg_9)]
avg_list += [sum(avg_10) / len(avg_10)]
avg_list += [sum(avg_11) / len(avg_11)]
avg_list += [sum(avg_12) / len(avg_12)]

#yellow bar graph

py.bar(months, avg_list, color = 'y')
py.plot(months, max_list, label = "High Temperature", color = 'r')
py.plot(months, min_list, label = "Low Temperature", color = 'b')
py.ylim(0, 100)
py.xlabel("Month")
py.ylabel("Average Temperature in F")
py.title("Temperature by Month")
py.legend(loc = 'upper left')
py.show()


weather_file.close()




