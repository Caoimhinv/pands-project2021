# pands-project2021
Fisher’s Iris data set

Problem statement
This project concerns the well-known Fisher’s Iris data set [3]. You must research the data set
and write documentation and code (in Python [1]) to investigate it. An online search for
information on the data set will convince you that many people have investigated it
previously. You are expected to be able to break this project into several smaller tasks that
are easier to solve, and to plug these together after they have been completed.
You might do that for this project as follows:
1. Research the data set online and write a summary about it in your README.
2. Download the data set and add it to your repository.
3. Write a program called analysis.py that:
• outputs a summary of each variable to a single text file,
• saves a histogram of each variable to png files, and
• outputs a scatter plot of each pair of variables. 

Intro
Fisher's Iris data set is a multivarate dataset introduced by statistician Ronald Fisher in his 1936 paper *The use of multiple measurements in taxonuic problems*. It was collected by botanist Edgar Anderson, whom it is also sometimes named after, "to quantify the morphologic variation of Iris flowers of three related species".
The data set consists of 50 samples from each of three species of iris - Iris setosa, Iris virginica and Iris versicolor. Four elements were measured from each - petals and widths of sepals and petals.

![Image of the 3 different species of Iris.](iris_images.png)

Above we can see what exactly what we're referring to.

## Process - initial number crunching
I downloaded the data as a csv file which can be viewed in the accompanying file <<iris_dataset.csv>>. I imported the **pandas**, **matplotlib.pyplot**, and **seaborn** modules to assist in the reading, analysis and visualisation of the data.
I read the file using the **.read_csv()** method and started some initial parsing of the data. I found the **.size()** and **.shape()** of the data, followed then by the column names (**.colums()**), and then printed out the first 5 lines of the data set using the **.head()** method. I used the **.describe()** method to delve a bit deeper into the data - this produced a lot of useful information such as the maximum and minimun values, the mean, and the standard deviation. I then isolated each species of iris using the **.groupby()** method and did the same analysis. I finished off this initial exploration by looking at correlation (**.corr()**) in the data.
The results can all be viewed in the outputted textfile <<outputted_iris_data_textfile.txt>>. 
## What did I discover??????
We can see straight away.........!

## part 2 visualisation
- scatter
Visualising data can make it easier to interpret. We began by creating scatter plots looking at the relationship between each pair of variables. We do this using **myplotlib.pyplot** and **seaborn.scatterplot()** and create 4 **.subplots()** - 1. sepal length v width; 2. sepal width v length; 3. petal length v width; 4. petal width v length. 
I've set a colour theme and grid style (**.set_style()**)for all of the visualisations. I've formatted a lot of the other elements including the various font sizes and names, and the legend.
The first thing that jumps out is that the setosa species is quite distinct from the other two in each of the aspects. In terms of sepal dimensions, versicoler and virginica are quite closely aligned but much less so when it comes to petal dimensions where we can see it bit of divergence.
![insert scatter plots maybe?](insert_image.png)

- kde
We can see the same data visualised here as a **kdeplot()** (kde = kernal density estimation). Again we can clearly see the setosa variety as distinct from the others. But we can see more clearly the centre kernal of both petal dimensions of the other two species more clearly defined.
![insert kde plots maybe?](insert_image.png)

-boxplot
Next I tried boxplots. Here we can see some of the same patterns, i.e. the setosa species distinct from the others. But can also define better the comparison between other two species in terms of petal dimensions. In this box plot, the horozontal line in the middle of each box represents the median value while the upper and lower limits of the box represent one standard deviation from there ( I think!). The outstretched arms with lines then represent the 25% and 75% quartiles (I think), while the diamonds represent outliers. What does that all mean!!!! :)

-swarmplot
This looks at the same data as the box plot. It's basically a scatter plot superimposed on a violin plot. I don't think it tells us anything we didn't know already but it looks nice and kind of like a flower (or a ray!)

-histograms
I created 4 subplots of histograms - one for each element. Again the same findings.

-pairplot
This gives us a good overview of the entire dataset. Here we can see a bit more daylight between the virginica and versicolor species when we compare some of the other non-related variuables against each other. In particular petal length against sepal length and width.

-heatmap
Correlation heatmap. We can see here the elements that are clearly correlated and those that aren't, e.g. sepal length with petal length and width; petal length and width; petal length and width with sepal length.
 











