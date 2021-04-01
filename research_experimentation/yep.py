import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.axes_style("darkgrid")
iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

f, axes = plt.subplots(2, 2)
# ax1. They are layed out in the form [0,0] where the first number represents the row and the second the column
# sns.jointplot(data=iris, x='sepal_length', y='sepal_width', kind='kde', ax=axes[0,0])

# sns.jointplot(data=iris, x='sepal_width', y='sepal_length', kind='kde', ax=axes[0,1])

# sns.jointplot(data=iris, x='petal_length', y='petal_width', kind='kde', ax=axes[1,0])

# sns.jointplot(data=iris, x='petal_width', y='petal_length', kind='kde', ax=axes[1,1])

# plt.show()

# iris_mx = iris.corr()
# sns.heatmap(iris_mx, annot=True, cmap="cubehelix")
# plt.show()

# species = iris.pop('species')
# versicolor = species
# print(versicolor.head())

# species = iris.pop('species')
# sns.clustermap(iris)
# plt.show()

print(iris.info())
