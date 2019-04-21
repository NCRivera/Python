# Import the necessary packages.
import pandas as pd
import matplotlib.pyplot as plt

# set url variable as the data I need, Daniel Chen github.
url = 'https://raw.githubusercontent.com/chendaniely/pandas_for_everyone/' \
    'master/data/gapminder.tsv'

# Read the data.
data = pd.read_csv(url, sep='\t')

# Using Afghanistan data.
afghan_data = data[data['country'] == 'Afghanistan']

# Checking the data
print(afghan_data.describe())

# Creating the overall figure. Setting the title.
fig = plt.figure()
fig.suptitle('Afghanistan Data')

# Creating the subplots, 2 small and 1 large.
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 1, 2)

# Life Expectancy
ax1.plot(afghan_data['year'], afghan_data['lifeExp'])
ax1.set(title='Life Expectancy', ylabel='Age')

# Population
ax2.plot(afghan_data['year'], afghan_data['pop'])
ax2.set(title='Population', ylabel='Amount')

# GDP
ax3.plot(afghan_data['year'], afghan_data['gdpPercap'])
ax3.set(title='GDP', ylabel='Dollars')

# Result
plt.show()
