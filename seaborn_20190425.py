# Importing the Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data set import
mpg_data = pd.read_csv('C:/Users/river/Data/mpg.csv')

print(mpg_data.head(n=3))

sns.set_style('darkgrid')

sns.relplot(x='displ', y='hwy', data=mpg_data)

sns.relplot(x='displ', y='hwy',
            hue='class',
            data=mpg_data)

sns.relplot(x='displ', y='hwy',
            hue='class', col='cyl',
            data=mpg_data)

plt.show()
