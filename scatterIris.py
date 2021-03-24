# Quick go at scatter plots. No idea yet of relevence!
# Author: Caoimhin Vallely

# ref https://www.activestate.com/resources/quick-reads/how-to-access-a-column-in-a-dataframe-using-pandas/

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/scatterIris.py")
sepal_length = iris['sepal_length']
sepal_width = iris['sepal_width']
petal_length = iris['petal_length']
petal_width = iris['petal_width']
species = iris['species']
plt.scatter(petal_length, sepal_length, color = 'r')
plt.scatter(petal_width, sepal_width, color = 'b')
plt.show()