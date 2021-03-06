
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# plt.style.use('fivethirtyeight')


df = pd.read_csv('./data/washington_data.csv', index_col='year')


df['wash_moving'] = df['wash_temp'].rolling(window=20, min_periods=1).mean()
df['global_moving'] = df['global_temp'].rolling(window=20, min_periods=1).mean()
df = df.round({'diff': 2, 'global_moving': 2, 'wash_moving': 2})

# Pull data into lists
year = df.index.tolist()[20:]
wash_actual = df['wash_temp'].tolist()[20:]
global_actual = df['global_temp'].tolist()[20:]
wash_temp = df['wash_moving'].tolist()[20:]
global_temp = df['global_moving'].tolist()[20:]

# print(year)
# print(wash_temp)
# print(global_temp)
# print(diff)

plt.plot(year, wash_actual, color='#EAC6FF', linewidth=2, label='Washington - Measured Temperature')
plt.plot(year, global_actual, color='#FFE1F7', linewidth=2, label='Global - Measured Temperature')
plt.plot(year, wash_temp, linewidth=3, color='#512D6D', label='Washington - Moving Average')
plt.plot(year, global_temp, linewidth=3, color='#F8485E', label='Global - Moving Average')

plt.xlabel('year')
plt.ylabel('Tempereature (°C)')
plt.title('Measured Temperature vs 20-year Moving Average')
plt.legend()
plt.tight_layout()

plt.savefig('actual_vs_moving.pdf')
plt.savefig('actual_vs_moving.png')
plt.show()


plt.plot(year, wash_temp, linewidth=2, color='#512D6D', label='Washington, DC')
plt.plot(year, global_temp, linewidth=2, color='#F8485E', label='Global')




plt.xlabel('year')
plt.ylabel('Tempereature (°C)')
plt.title('Global vs. Washington Temperature (20-year Moving Average)')

plt.fill_between(year, wash_temp, global_temp, alpha=0.1)
plt.legend()
plt.tight_layout()




plt.savefig('city_vs_global_analysis.pdf')
plt.savefig('city_vs_global_analysis.png')
plt.show()



plt.scatter(year[-33:], wash_temp[-33:], linewidth=1, color='#512D6D', label='Washington, DC', marker='.')
plt.scatter(year[-33:], global_temp[-33:], linewidth=1, color='#F8485E', label='Global', marker='.')

# Add Marker to the points with values
plt.scatter(year[-33:][0], wash_temp[-33:][0], linewidth=3, color='#512D6D', marker="v")
plt.scatter(year[-33:][-1], wash_temp[-33:][-1], linewidth=3, color='#512D6D', marker="v")
plt.scatter(year[-33:][0], global_temp[-33:][0], linewidth=3, color='#F8485E', marker="^")
plt.scatter(year[-33:][-1], global_temp[-33:][-1], linewidth=3, color='#F8485E', marker="v")


plt.annotate(str(wash_temp[-33:][0]) + '°C', xy=( year[-33:][0], wash_temp[-33:][0]), xytext=(1980, 11.7))
plt.annotate(str(wash_temp[-33:][-1]) + '°C' , xy=( year[-33:][-1], wash_temp[-33:][-1]), xytext=(2011.5, 12.5))

plt.annotate(str(global_temp[-33:][0]) + '°C', xy=( year[-33:][0], global_temp[-33:][0]), xytext=(1980, 9))
plt.annotate(str(global_temp[-33:][-1]) + '°C' , xy=( year[-33:][-1], global_temp[-33:][-1]), xytext=(2011, 9 ))


m, b = np.polyfit(year[-33:], wash_temp[-33:], 1)
m1, b1 = np.polyfit(year[-33:], global_temp[-33:], 1)
plt.text(1990, 12, f'm = {round(m, 4)}', color='#512D6D', fontsize=15)
plt.text(1990, 9.2, f'm = {round(m1, 4)}', color='#F8485E', fontsize=15)

line = []
line1  = []
for y in year[-33:]:
    line.append((m * y) + b)

for y in year[-33:]:
    line1.append((m1 * y) + b1)

plt.plot(year[-33:], line)
plt.plot(year[-33:], line1)


plt.xlabel('year')
plt.ylabel('Tempereature (°C)')
plt.title('Temperatures - 1980 to 2013- with regression lines')

plt.legend()
plt.tight_layout()




plt.savefig('since_1950.pdf')
plt.savefig('since_1950.png')
plt.show()
