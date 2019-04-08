import pandas as pd

# Pandas for Everyone turned me to this dataset
gapminder = pd.read_csv('C:/Data/gapminder.tsv', sep='\t')

# Slicing the continent Americas out of the dataset
gapminder_americas = gapminder[gapminder['continent'] == 'Americas']

# New series by Applying the GroupBy to Year, pass mean() life expectancy
# 
americas_avrg_lf = gapminder_americas.groupby('year')['lifeExp'].mean()

# Creating an index to use in my plot.
idx = pd.Series(americas_avrg_lf.index.values)

# Plotting
import matplotlib.pyplot as plt

plt.plot(idx, americas_avrg_lf)
plt.title('Average Life Expectancy by Year - Americas')
plt.xlabel('Years')
plt.ylabel('Life Expectancy')

# Show and Tell~
plt.show()
