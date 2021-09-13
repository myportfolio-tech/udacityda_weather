import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/washington_data.csv', index_col='year')
print(df.head())


wash_plot = df['wash_temp'].rolling(window=10).mean().plot(figsize=(10, 6), label='city')

global_plot = df['global_temp'].rolling(window=10).mean().plot(figsize=(10, 6), label='global')

diff_plot = (df['wash_temp'] - df['global_temp']).rolling(window=10).mean().plot(figsize=(10, 6), label='difference')
diff_plot.legend(['city temp', 'global temp','difference'])


plt.savefig('temperatures.pdf')
plt.show()