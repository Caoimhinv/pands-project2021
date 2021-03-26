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

18/03/21
Dataset copied and pasted from https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv

Bit of background
https://en.wikipedia.org/wiki/Iris_flower_data_set
https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5

20/21 March
Just finding my feet!
Getting used to accessing, reading, parsing the data.
Did some simple calculations. Overall average measurements and then individual averages for each species.
Did a simple scatter plot - no idea the relevance just yet!
Think I'll carry on like this for a while and see where it leads!

23 March
After pandas lecture I discovered a few new tricks which make things a lot simpler! Firther investigation of pandas required! Now I have this new data, I need to try and understand what it means!
Think I've created all the plots, but they're all stuck on top of each other!

26 March
Scatter plots
Just getting to grips with these!
I'm interpretting a scatter plot of each pair of variables' as 12 plots 4 variables x the other 3. Nothing to be gleaned from comparing a variable against itself, although an example online seemed to have a histogram in that place, maybe just to keep the shape?

So after a lot of messing with figure() with all the plots sittin on top of each other, I discovered it's not what I want after all! plt.subplots(4,4) is the boy!
Not to make it look nicer and try to deal with the same variable comparison issue.

Update:
I've space it all out much better.
After a lot of searching I worked out the legend situation. For the moment I've filled the 4 empty boxes with legends.
I've only included the x,y markers on the outside plots to try and make it look tider - may revise.
I've scaled them all the same - i.e. 0-8 - to make it easier to compare - not sure if appropriate? If I let them all go to defualt it might be easier to read or at least interpreate if anything useful is happening on an indiviudal level?

Update:
Started work on histograms. Distribution of each variable between the species

Intro
So we're dealing with a dataset introduced by statistician Ronald Fisher and collected by botanist Edgar Anderson. It consists of 50 samples from each of three species of iris - Iris setosa, Iris virginica and Iris versicolor. Four elements were measured from each - petals and widths of sepals and petals.

![Image of Irises](/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_images.png)

Does this work?
ref - https://morioh.com/p/eafb28ccf4e3



