# Quick go at scatter plots. No idea yet of relevence!
# Author: Caoimhin Vallely

# ref https://www.activestate.com/resources/quick-reads/how-to-access-a-column-in-a-dataframe-using-pandas/

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("irisDataset.csv")
sepalLength = iris['sepal_length']
sepalWidth = iris['sepal_width']
petalLength = iris['petal_length']
petalWidth = iris['petal_width']
species = iris['species']
plt.scatter(petalLength, sepalLength, color = 'r')
plt.scatter(petalWidth, sepalWidth, color = 'b')
plt.show()