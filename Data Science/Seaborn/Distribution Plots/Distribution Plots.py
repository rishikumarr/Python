import seaborn as sns
from matplotlib import pyplot as plt

tips=sns.load_dataset("tips") # DataFrame(Comes inbuild with SeaBorn)

##################################################### Dist Plot #########################################################################

# sns.distplot(tips["total_bill"])
# sns.distplot(tips["total_bill"],kde=False) # DistPlot Without KDE(Kernel Density Estimation)

# plt.title('Dist Plot')

##################################################### Joint Plot ########################################################################

# sns.jointplot(x="total_bill",y="tip",data=tips) # Default Joint Plot
# sns.jointplot(x="total_bill",y="tip",data=tips,kind="hex") # Hexagon Distribution
# sns.jointplot(x="total_bill",y="tip",data=tips,kind="reg") # Regression Distribution
# sns.jointplot(x="total_bill",y="tip",data=tips,kind="kde") # KDE Distribution

# plt.title('Joint Plot')

##################################################### Pair Plot #########################################################################

# sns.pairplot(tips)
# # sns.pairplot(tips,hue="smoker")                     # Lets Plot Smoker Column
# # sns.pairplot(tips,hue="sex")                        # Lets Plot Sex Column
# sns.pairplot(tips,hue="smoker",palette="coolwarm")    # Lets add Palette

# plt.title('Pair Plot')

##################################################### Rug Plot ##########################################################################

# sns.rugplot(tips["total_bill"])

# plt.title('Rug Plot')
##################################################### KDE Plot ###########################################################################

# sns.kdeplot(tips["total_bill"])

# plt.title("KDE Plot")


##################################################### Pair Grid #########################################################################

# sns.PairGrid(tips)

# plt.title('Pair Grid')


plt.show()
