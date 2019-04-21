# Plotting a comparison of Life Expectancies of US Vs. Afghnistan
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/chendaniely/pandas_for_everyone/' \
    'master/data/gapminder.tsv'

data = pd.read_csv(url, sep='\t')


x_data = pd.Series(data['year'].unique())

# Slicing the data from the dataset.
afghan_data = data[data['country'] == 'Afghanistan']
us_data = data[data['country'] == 'United States']

# Slicing the lifeExp from the sliced dataset.
us_life = us_data['lifeExp']
afg_life = afghan_data['lifeExp']

# Plotting both series.
plt.plot(x_data, us_life, 'r*--')
plt.plot(x_data, afg_life, 'g.:')

# Add grid.
plt.grid()

# Title
plt.title('Life Expectancy Comparison\nUS & Afghanistan')

# Setting Y ticks and label
y_tks = list(range(25,85, 5))
plt.yticks(ticks=y_tks)
plt.ylabel('Age')

# Setting X ticks and label
plt.xticks(ticks=x_data)
plt.xlabel('Year')

# Results
plt.show()
