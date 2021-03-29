# creating a scatter matrix plot for all the variables
# Author: Caoimhin Vallely

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv')

sns.pairplot(iris, hue="species",markers=["o", "s", "D"], palette=['y','b','g'])
plt.show()



