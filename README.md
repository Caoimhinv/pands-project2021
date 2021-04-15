# Fisher’s Iris dataset analysis project  
## Programming and Scripting module 2021  
## Caoimhin Vallely

-----
## Intro  
Fisher's Iris dataset is a multivarate dataset named after the statistician Ronald Fisher who introduced it in his 1936 paper *"The Use of Multiple Measurements in Taxonic Problems* which was published in the journal *'Annals of Eugenics'*. The original data was collected by botanist Edgar Anderson, whom it is also sometimes named after, with the aim *"to quantify the morphologic variation of Iris flowers of three related species"*.  

### Background
The dataset consists of 50 samples from each of three species of iris - Iris setosa, Iris virginica and Iris versicolor. Four attributes were measured from each sample - lengths and widths of both sepals and petals in cemtimetres. The samples from the setosa and versicolar were were all collected on the same day from the same field by the same person. The third species was collected elsewhere.

- the following image shows the 3 species of Iris involved and what the petals and sepals actually are: 

![Image of the 3 different species of Iris.](./Images/image_of_irises.png)

We already have a few terms that required looking up!  
>**Taxonomy** - *"... the scientific study of naming, defining and classifying groups of biological organisms based on shared characteristics."*  
>**Linear discriminant analysis** - *"... method used in statistics and other fields, to find a linear combination of features that characterizes or separates two or more classes of objects or events."*  
>**Multivariate statistics** - *"... a subdivision of statistics encompassing the simultaneous observation and analysis of more than one outcome variable."*  
>**Morphology** - *"... the form and structure of an organism or one of its parts."*  

I felt a good place to start was reading Ronald Fisher's original paper. I found this quite a diffcult read, with a lot of statistical terminology and methodology that is beyond my level of understanding at this point. What I did understand was very interesting though, and what impressed me most was that he did all of this without a calculator or computer!

The wikipedia entry on the dataset, along with some more general background information, tells us that the dataset has become an important testcase in many fields. Although the paragragh on uses of the dataset focuses mostly on machine learning which is outside the breadth of this module.

The article *The Iris Dataset — A Little Bit of History and Biology* by Yong Cui gives a more general overview of the dataset, and to me at least, is a bit more accessible. We get some more background on each of the main protagonists and their further contributions to their respective fields.
It's quite interesting to find out that although Fisher developed this model to discriminate between the species, botanists (including Anderson himself), discovered that seed size a more reliable differentiator. My experience of, and interest in gardening has up until this point exceded that of statistics so this gave me a chuckle :smile:! Anyway, the main takeaway from this article for me, is that appreciating and trying to understand something about the actual data subject matter is important, and one shouldn't just focus on the figures in isolation.

In preparation, I did some revision (and learning!) of basic statistical methods. However, apart from that, I haven't ventured outside the subject matter and methods covered in the lectures to date. There was a temptation to delve into machine learning, which it is suggested this dataset is quite appropriate for, but I resisted, reckoning I'd be better equipped for that further down the line.

## part 1 - initial data exploration
### 1.1
My first step was to download the dataset which I did from <https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv> and save it as the csv (comma separated value) file <iris_dataset.csv> in this repositry. I cross referenced this with another, more authentic looking version from https://archive.ics.uci.edu/ml/datasets/Iris but they were identical.
I imported the **pandas**, **csv**, **matplotlib.pyplot**, and **seaborn** libraries to assist in the reading, analysis and visualisation of the data.
- **pandas** - > "... is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language."
- **csv** - > "The csv library provides functionality to both read from and write to CSV files."
- **matplotlib.pyplot** - > "...is a state-based interface to matplotlib. It provides a MATLAB-like way of plotting. Pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation."
- **seaborn** - > "... is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics."

These are imported as per convention, and economy of space, as **pd**, **plt**, and **sns** respectively.

I read the file using **pandas** with the following:

    iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

### 1.2
*Note: the program writes a summation of all of the following findings to the text file <outputted_iris_data_textfile.txt>, a copy of which is inclued in this repositry.*  
  
I was then able to start some initial parsing of the data. I found the **.size()** and **.shape()** of the data, followed then by the column names (**.columns()**). **.isnull()** tells me there are no missing values in the dataset. I then printed out the first and last 5 lines of the data set using the **.head()** and **.tail()** tools, plus a random/sample 5 rows using the **.sample()** tool.   
We can see that there are 750 entries divided into 150 rows and 5 columns. The columns are titled 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', and 'species'. The printout of the first 5 rows shows that they are all the same species - 'setosa' - and that all the values are 5.1 and less, with the sepal being considerably bigger than the petal. The last 5 rows are all of the 'virginica' species, with the dimensions being quite different but less of a variance between sepal and petal size. The sample 5 rows printed out show a 3rd species, versicolor, and also display a siginificant range in values in the petal dimensions. **.value_counts()** tells me that the 150 rows are divided evenly between these 3 species.

### 1.3
I used the **.describe()** method to delve a bit deeper into the data. This produced a lot of useful information such as the maximum and minimum values, the mean, and the standard deviation. We can quickly see that what was suggested above in relation to the petal dimensions is very much in evidence with quite a significant range between the lowest and highest petal length (1.0 - 6.9) and a standard deviation of 1.76.
To dig further we needed to apply the same method to each variety in isolation. I did this first with **.groupby()** but that produced 32 columns which weren't that easy to read! The following command ran on each species worked better:

    iris.loc[iris['species'] == "setosa"].describe()

The first major point to emerge is that the setosa species has a much lower mean petal length and width than the other 2 varieties. The virginica has the highest mean petal length but surprisingly the setosa has the highest mean petal width. The standard deviations are all much lower suggesting much less variance when each species is taken in isolation.  

I then looked at correlation in the dataset with the **.corr()** tool. This reveals stong correlation between petal width and length, but considerably less between sepal length and width. Interestingly there is also a strong correlation between sepal length and both petal length and width.

Next, I created a **.copy()** of the iris dataset **iris2** so I could don some perform some further calculations on it without affecting the rest of the subsequent code. I decided to add all of the attributes on each row and create a new column entitled **totals**. I also created a column for the **mean** of each row. A version of this new dataset is saved as a csv file entitled **iris_data_sets_with_totals.csv** in the repositry.
I then isolated each species and printed the **head** of each with the new columns, and then calculated the mean and standard deviation for the **totals** column. I could have used **describe()** again but I'm not sure how much useful extra information that would produce. We can clearly see a distinction here with the setosa species appearing considerably smaller, with a relatively low standard deviation. The others are a little closer in dimension with a higher SD.

All of the above calculations, along with some formatting, were saved as variables and then printed to the file <outputted_iris_data_textfile.txt> using the **writeslines()** method. This file can be viewed in the repositry.

## part 2 - visualisation

Visualising data can make it much easier to interpret and present, so I put a lot of energy into this aspect of the project. The libraries **matplotlib.pyplot** and its relative **seaborn** contain many powerful and highly effective analysis and visualisation tools, so I endeavoured to get the most of them that I could.
I've set a global colour theme and grid style (**.set_style()**) for all of the visualisations to give a bit of consistency. I spent a lot of time formatting a lot of the stylitic elements including the various font sizes and styles; the legends; marker sizes and styles; linestyles and sizes, etc. This was both to make everything more aesthetically pleasing and also to make the information clearer and easier to interpret and understand.

### 2.1
- **heatmap**
We begin by creating a heatmap based on the correlation we investigated above. We save **iris.corr()** as the variable **iris_hm** and then create the heatmap with seaborn **sns.heatmap()**. **annot=True** prints the values on each square, while **cmap="cubehelix"** is the colour palette used. Unfortunately my own colour themes weren't really that effective here so I went with one of the defaults.  

![heatmap](./Images/heatmap.png)  

The findings are very clear when presented like this with the darker areas representing the least correlation and vice versa.  

### 2.2
- **box plot**  
>"A boxplot is a standardized way of displaying the distribution of data based on a five number summary (“minimum”, first quartile (Q1), median, third quartile (Q3), and “maximum”). It can tell you about your outliers and what their values are. It can also tell you if your data is symmetrical, how tightly your data is grouped, and if and how your data is skewed."

![boxplot explained](./Images/box_plot_explained2.png)

The box plot seemed to be the best place to start to get an overall impression of the data. We started with an overall boxplot taking in all of the data at once:

![overall boxplot](./Images/boxplot.png)

I created this boxplot with seaborn **sns.boxplot()**. I formatted the **linewidth** and **fliersize** (diamonds representing outliers), and set the colour palette to my customised **color_theme2**. I formatted the **ticks_params** a little (**axis='both', which='major', labelsize=7**), and the **ylabel** - **"(cm)", fontsize=7, fontname='fantasy'**. I'm using the **fantasy** font and trying to use the same fontsizes globally for each element for consistency. The xlabel didn't need anything more than the class names which are there by default.

We can see here clearly all the relative dimensions of each element. Sepal_length has the greatest individual value, and highest median value, while petal_width has the smallest individual value and lowest median. Petal_length has the greatest dispersion while the sepal width has the least. We saw this information already in the text analysis above but it is much easier to appreciate when presented in this manner. A normal distribution would be where all 4 quartiles are relatively even. We can see here that sepal_length is the closest in that regard, while both petal dimensions are quite skewed. Sepal_width contains quite a few outliers.

To find out more we need to isolate the attributes and see what is happening within each individual class. 

![separated boxplot](./Images/boxplot1.png)

I've created a grid here of 4 boxplots here using the **plt.subplots()** tool. **(2,2)** defines 2 rows and 2 columns. Within the code for each boxplot I've defined the position, e.g. **ax=axes[0,1]** where the first digit is the row and the second the column (with the 0 being the first row and 1 being the 2nd column). I've formatted all of the same elements as above trying to maintain consistency in the style.

Here we can see the setosa species emerging as being quite distinct from the others particularly in terms of petal length and width. But we can also define somewhat of a difference between the other two species in terms of petal dimensions.

### 2.3  
- **violin plot**  
>"A violin plot plays a similar role as a box ... plot. It shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared. Unlike a box plot, in which all of the plot components correspond to actual datapoints, the violin plot features a kernel density estimation of the underlying distribution."

![insert violin plots here](./Images/violinplot.png)

This violin plot is created using seaborn **sns.violinplot()**. The formatting is nearly the same as the boxplot except an extra element **inner='point'** is defined - this refers to the data points inside the plot.

We can get some extra understanding of same data here. We can see a split in the petal visualisation suggesting some discrimination between the classes.  

- **strip plot**  
>"a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution."

These are in effect violin plots with the data points 'scattered' to represent the distribution of values. I've isolated each of the classes out again and we can see the pattern more clearly. The setosa petal again emerges distinct from the other species when we look at the petal dimensions.

![insert strip plots here](./Images/stripplot.png)

We created these by first defining the grid as we did with the boxplots **plt.subplots**, then the violin plot as above **sns.violinplot**, and then **sns.stripplot**. The extra formatting for the stripplot concerns the data points - **size=2, color='white', edgecolor='black', linewidth=.5**. A bit of time was spent experimenting with the right combination for each of these to maximise legibility. This actually started out as a **swarmplot**, which adjusts the locations of the data points to avoid overlap, but this was proving problematic with the code. VSC was suggesting making the data points smaller and smaller until it got to the point they were becoming irrelevent! Stripplot while not as pretty and symmetrical behaved better in this regard.

### 2.4  
- **histogram**  
histograms are the most commonly used graph to show frequency distributions. I've created 4 subplots of histograms - one for each variable. 

![insert histogram plots here](./Images/histogram.png)

We created these 4 histograms - 1 for each attribute - and again positioned them on a 2x2 grid using **plt.subplots**. A few extra elements were involved in the formatting here:

    sns.histplot(data=iris, x='sepal_length', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, legend=False, ax=axes[0,0]

**binwidth=0.1** refers to the value parameters of each 'bar'. I experimeted increasing and decreasing this but this seemed to fir best.
**hue='species'** this separates the classes so we can see them all clearly side by side
**kde=True** kde is kernal density estimation. It draws a continuous curved line which estimates the values between the data points
**alpha=0.5** this allows some blended of the data so that one doesn't overlap the other
**legend=False** as the legend is the same for all I've only included it on one.
We've already seem **palette** and **ax** before.

From these histograms, we can clearly see the same pattern as above with the setosa petal quite separate to the others. The KDE also shows the relative relationships to normal distribution, the most notable aspect of which is the narrowness, and proxomity to the mean, of the petal attributes of the setosa species.

### 2.5
Up until now all of the plotting has involved looking at one numeric parameter at a time. This kind of analysis is called **univariate analysis**. By looking at a second variable and the relationship between the two we are extending our analysis into **bivariate analysis**. Scatterplots are the simplest and most common method to explore this.  

- **scatter plot**
>"A scatterplot is a graphic representation of points referencing two variables. To create a scatterplot, two variables are observed and plotted on a graph. The resulting display demonstrates the relationship between the variables. The relationship is strongest where the points are clustered closest together."

![insert pairgrid Scatter here](./Images/pairgrid1.png)

I've used the seaborn **.PairGrid()** tool to create a **scatterplot matrix** where each combination of variable is plotted against each other. The four diagonal boxes show more histograms. 

Below is another visualisation of the same data this time using KDE (kernal density estimation), which is a technique that uses probability estimation to create a smooth curve. While normally used with histograms, I think it works well here and looks visually pleasing and less cluttered than the scatter plots while revealing the same information

![insert pairgrid KDE here](./Images/pairgrid2.png)

Again we can see clearly that the setosa species is quite distinct from the other two in each of the variables, especially petal dimensions. In terms of sepal dimensions, versicolar and virginica are quite closely aligned, but less so when it comes to petal dimensions where we can see a bit of divergence. However it doesn't quite separate them.

## conclusion
Most of the literature I read when embarking on this project suggested that only one species, setosa, could be separated linearly. This was quite clearly borne out through all of my analysis. There does appear to be another method that can discriminate between the other two species - **nonlinear principal component analysis** - though the scary wikipedia entry convinces me to leave that to another day :confused:!  
A further progression on this project would be to create an algorithim to test whether we could predict the species just from the attributes. I presume we'll be looking into this area later in the course.

## Guide to files in the repositry
- The **Images** folder contains all of the visualisations created by the python script (**analysis.py**) that are included above. Plus a few other downloaded example images from the web.
- **.gitignore** is an automatically generated text file that tells Git which files or folders to ignore in a project.
- **README.md** is this!
- **analysis.py** is the main script. The program carries out statistical analysis on the dataset and prints out the results to the text file **outputted_iris_data_textfile.txt**. It also creates the series of data visualisations contained in the **Images** folder. 
- **iris_dataset.csv** is the original dataset
- **iris_dataset_with_totals.csv** is the dataset with extra columns - row totals, and row means.
- **notes.txt** is a rough journal of my progress through the project.
- **outputted_iris_data_textfile.txt** is the data analysis created by the main program script **analysis.py**

## References  

### Background and source code
- *THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC PROBLEMS* by R. A. Fisher (the original) - https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x
- *Taxonomy* - https://en.wikipedia.org/wiki/Taxonomy_(biology)
- *Linear Discriminant Analysis* - https://en.wikipedia.org/wiki/Linear_discriminant_analysis
- *Iris Data Set* (source for code and some background) - https://archive.ics.uci.edu/ml/datasets/Iris
- *Another source for code* - https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv
- *Iris flower data set* (Wikipedia) - https://en.wikipedia.org/wiki/Iris_flower_data_set
- *The Iris Dataset — A Little Bit of History and Biology* by Yong Cui - https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
- *Basic statistics* - https://www.statisticshowto.com/statistics-basics/
- *Quantitative Data: Definition, Types, Analysis and Examples* - https://www.questionpro.com/blog/quantitative-data/
- *Your Guide to Qualitative and Quantitative Data Analysis Methods* - https://humansofdata.atlan.com/2018/09/qualitative-quantitative-data-analysis-methods/
- *Markdown* - https://www.markdownguide.org/basic-syntax/
- *Images in markdown* - https://stackoverflow.com/questions/41604263/how-do-i-display-local-image-in-markdown

### Initial data exploration
- *Exploratory Data Analysis of IRIS Data Set Using Python* by Venkata Sai Reddy Avuluri - https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
- *Python File writelines() Method* - https://www.w3schools.com/python/ref_file_writelines.asp
- *Python – Basics of Pandas using Iris Dataset* - https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
- *Reading and Writing CSV Files in Python* - https://realpython.com/python-csv/
- *How to Export Pandas DataFrame to CSV* - https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03
- *Python Set copy() Method* - https://beginnersbook.com/2019/03/python-set-copy-method/#:~:text=The%20copy()%20method%20in,()%20method%20instead%20of%20%3D%20operator.
- *Source for irises image* - https://morioh.com/p/eafb28ccf4e3
- *round when sending to .csv file* - https://github.com/pandas-dev/pandas/issues/13159
- *writelines()* - https://www.w3schools.com/python/ref_file_writelines.asp

### Data visualisation

#### pandas/matplotlib.pyplot
- *matplotlib.pyplot* - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
- *Scatter plots* - https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.scatter.html
- *How to Set Axis Range (xlim, ylim) in Matplotlib* - https://stackabuse.com/how-to-set-axis-range-xlim-ylim-in-matplotlib/
- *Multiple subplots* - https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html#sphx-glr-gallery-subplots-axes-and-figures-subplot-py
- *Set a Single Main Title for All the Subplots in Matplotlib* - https://www.delftstack.com/howto/matplotlib/how-to-set-a-single-main-title-for-all-the-subplots-in-matplotlib/
- *Legend* - https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/
- *Legends in subplot* - https://stackoverflow.com/questions/27016904/matplotlib-legends-in-subplot
- *Creating multiple subplots using plt.subplots* - https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
- *Python Histogram Plotting: NumPy, Matplotlib, Pandas & Seaborn* - https://realpython.com/python-histograms/#visualizing-histograms-with-matplotlib-and-pandas
- *Matplotlib make tick labels font size smaller* - https://stackoverflow.com/questions/6390393/matplotlib-make-tick-labels-font-size-smaller
- *set_linestyle* - https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle
- *How to use Pandas Scatter Matrix (Pair Plot) to Visualize Trends in Data* by Erik Marsja - https://www.marsja.se/pandas-scatter-matrix-pair-plot/
- *Pair plots using Scatter matrix in Pandas* - https://www.geeksforgeeks.org/pair-plots-using-scatter-matrix-in-pandas/
- *List of named colors in matplotlib* - https://matplotlib.org/stable/gallery/color/named_colors.html
- *Understanding Boxplots* (and source for 'boxplots explained' image) by Michael Galarnyk - https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51
- *Interpretting boxolots* - https://www.simplypsychology.org/boxplots.html#:~:text=Box%20plots%20are%20useful%20as%20they%20show%20the%20skewness%20of,then%20the%20distribution%20is%20symmetric. 

#### Seaborn
- *Seaborn Tutorial 2020* (YouTube) by Derek Banas - https://www.youtube.com/watch?v=6GUZXDef2U0
- *seaborn.pairplot* - https://seaborn.pydata.org/generated/seaborn.pairplot.html
- *seaborn.histplot* - https://seaborn.pydata.org/generated/seaborn.histplot.html
- *seaborn.scatterplot* - https://seaborn.pydata.org/generated/seaborn.scatterplot.html
- *seaborn.kdeplot* - https://seaborn.pydata.org/generated/seaborn.kdeplot.html
- *seaborn.violinplot* - https://seaborn.pydata.org/generated/seaborn.violinplot.html
- *seaborn.swarmplot* - https://seaborn.pydata.org/generated/seaborn.swarmplot.html
- *Subplot for seaborn boxplot* - https://stackoverflow.com/questions/41384040/subplot-for-seaborn-boxplot
- *Building structured multi-plot grids in seaborn* - https://seaborn.pydata.org/tutorial/axis_grids.html
- *Choosing color palettes in seaborn* - https://seaborn.pydata.org/tutorial/color_palettes.html
- *How To Change Edge Color on Seaborn Scatter Plot* - https://datavizpyr.com/change-edge-color-on-seaborn-scatter-plot/
- *Seaborn Title Position* - https://stackoverflow.com/questions/52096050/seaborn-title-position
- *KDE Plot Visualization with Pandas and Seaborn* - https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/












