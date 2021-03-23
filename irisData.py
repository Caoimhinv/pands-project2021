# a quick introduction and overview of the data
# Author: Caoimhin Vallely

import pandas as pd

iris = pd.read_csv('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/irisDataset.csv')

# gives an overview on the data
iris_stats = iris.describe()
print(iris_stats)

# finds correlation between all of the data
iris_correlation = iris.corr()
print (iris_correlation)