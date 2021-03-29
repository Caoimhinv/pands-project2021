# experimenting with histograms in seaborn
# Author: Caoimhin Vallely

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

sns.histplot(data=iris, binwidth=0.1)

sns.histplot(data=iris, x='sepal_length', binwidth=0.1, hue='species', kde=True)

sns.histplot(data=iris, x='sepal_length', binwidth=0.1, hue='species', multiple="stack", kde=True)
plt.show()
