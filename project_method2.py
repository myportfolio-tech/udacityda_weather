import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/washington_data.csv', index_col='year')
print(df.head())

wash_temp = df['wash_temp'].tolist()
global_temp = df['global_temp'].tolist()
year = df.index.tolist()


# print(wash_temp)
# print(global_temp)
# print(year)

ymax = max(wash_temp)
ymin = max(global_temp)

fig = plt.figure(figsize=(16,10), dpi=300)


plt.plot(year, wash_temp, marker=".", color="#5bc0de")
plt.plot(year, global_temp, marker=".", color="#E8743B")



# wash_plot = df['wash_temp'].rolling(window=10).mean().plot(figsize=(10, 6), label='city')

# global_plot = df['global_temp'].rolling(window=10).mean().plot(figsize=(10, 6), label='global')

# diff_plot = (df['wash_temp'] - df['global_temp']).rolling(window=10).mean().plot(figsize=(10, 6), label='difference')
# diff_plot.legend(['city temp', 'global temp','difference'])


# plt.savefig('temperatures.pdf')
# plt.show()



