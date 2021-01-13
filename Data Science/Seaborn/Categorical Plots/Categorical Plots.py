import seaborn as sns

import numpy as np

from matplotlib import pyplot as plt

tips=sns.load_dataset("tips")

########################################################### Bar Plot #######################################################################

# sns.barplot(x="smoker",y="total_bill",data=tips) # this will show the mean of total_bill

# sns.barplot(x="smoker",y="total_bill",data=tips,estimator=np.std) # this will show the standard deviation of total_bill

########################################################### Count Plot #######################################################################

# sns.countplot(x="smoker",data=tips)

# plt.title("Count Plot")

########################################################### Box Plot #######################################################################

# sns.boxplot(x='day',y='total_bill',data=tips)

# sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker') # plotting along with extra information by adding hue

# plt.title("Box Plot")

########################################################### Violin Plot #######################################################################

# sns.violinplot(x="day",y="total_bill",data=tips)   # x= Categorical y= Numerical

# sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True) # plotting along with extra information by adding hue

# plt.title("Violin Plot")

########################################################### Strip Plot #######################################################################

# sns.stripplot(x="day",y="total_bill",data=tips)    # x= Categorical y= Numerical

# sns.stripplot(x="day",y="total_bill",data=tips,jitter=True) # jitter add space between dots

# sns.stripplot(x="day",y="total_bill",data=tips,jitter=True,hue='sex') # plotting along with extra information by adding hue

# sns.stripplot(x="day",y="total_bill",data=tips,jitter=True,hue='sex',dodge=True) # Split Dots according to data given in hue (Split/Dodge)

# plt.title("Strip Plot")

########################################################### Swarm Plot #######################################################################

# Swarm plot is the combination of stripplot and scatterplot in violinplot

# sns.swarmplot(x="day",y="total_bill",data=tips)       # x= Categorical y= Numerical

                                            # Now lets combine the above plot as violinplot

# sns.violinplot(x="day",y="total_bill",data=tips)

# sns.swarmplot(x="day",y="total_bill",data=tips,color="black")

# plt.title("Swarm Plot")

######################################################## Factor Plot / CatPlot #######################################################################

# sns.catplot(x="day",y="total_bill",data=tips,kind="bar")  # in kind we can specify the kind of the plot   # x= Categorical y= Numerical

# sns.catplot(x="day",y="total_bill",data=tips,kind="violin")

plt.show()
