# few simple calculations on overall dataset
# Author: Caoimhin Vallely

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/irisDataset.csv")
sepalLength = iris['sepal_length']
sepalWidth = iris['sepal_width']
petalLength = iris['petal_length']
petalWidth = iris['petal_width']
species = iris['species']

# histogram for distribution of petal length for all varieties
# hist ref: https://realpython.com/python-histograms/#visualizing-histograms-with-matplotlib-and-pandas
# plt.hist(petalLength, bins=80)
# plt.show()
# interesting but need to isolate each of the varieties

# sets up 4 plots - 2x2. All sharing the same x and y
fig, axs = plt.subplots(2,2, sharex=True, sharey=True)

# isolating the petal length of each
setosa_petal_lenth = petalLength[0:50]
varsicolor_petal_length = petalLength[50:100]
virginica_patel_length = petalLength[100:150]

axs[0,0].hist(setosa_petal_lenth, bins=35, color = 'y', label='setosa')
axs[0,0].hist(varsicolor_petal_length, bins=35, color = 'b', label='varsicolor')
axs[0,0].hist(virginica_patel_length, bins=35, color = 'r', label='virginica')
axs[0,0].set_ylabel("Frequency", fontsize=8)
axs[0,0].set_xlabel("Petal length (cm)", fontsize=8)
axs[0,0].legend(frameon=False, fontsize=8)

setosa_petal_width = petalWidth[0:50]
varsicolor_petal_width = petalWidth[50:100]
virginica_patel_width = petalWidth[100:150]

axs[0,1].hist(setosa_petal_width, bins=35, color = 'y', label='setosa')
axs[0,1].hist(varsicolor_petal_width, bins=35, color = 'b', label='varsicolor')
axs[0,1].hist(virginica_patel_width, bins=35, color = 'r', label='virginica')
axs[0,1].set_xlabel("Petal width (cm)", fontsize=8)
axs[0,1].legend(frameon=False, fontsize=8)

setosa_sepal_lenth = sepalLength[0:50]
varsicolor_sepal_length = sepalLength[50:100]
virginica_sepal_length = sepalLength[100:150]

axs[1,0].hist(setosa_sepal_lenth, bins=35, color = 'y', label='setosa')
axs[1,0].hist(varsicolor_sepal_length, bins=35, color = 'b', label='varsicolor')
axs[1,0].hist(virginica_sepal_length, bins=35, color = 'r', label='virginica')
axs[1,0].set_ylabel("Frequency", fontsize=8)
axs[1,0].set_xlabel("Sepal length (cm)", fontsize=8)
axs[1,0].legend(frameon=False, fontsize=8)

setosa_sepal_width = sepalWidth[0:50]
varsicolor_sepal_width = sepalWidth[50:100]
virginica_sepal_width = sepalWidth[100:150]

axs[1,1].hist(setosa_sepal_width, bins=35, color = 'y', label='setosa')
axs[1,1].hist(varsicolor_sepal_width, bins=35, color = 'b', label='varsicolor')
axs[1,1].hist(virginica_sepal_width, bins=35, color = 'r', label='virginica')
axs[1,1].set_xlabel("Sepal width (cm)", fontsize=8)
axs[1,1].legend(frameon=False, fontsize=8)

plt.suptitle('Distibrution of each variable')
plt.show()
# next I need to look at SD! https://www.advsofteng.com/doc/cdpydoc/histogram.htm

