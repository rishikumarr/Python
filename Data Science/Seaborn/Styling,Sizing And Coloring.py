import seaborn as sns
from matplotlib import pyplot as plt
tips=sns.load_dataset("tips")
# print(tips)
                                            # Adding ticks
# sns.set_style('ticks')
# sns.countplot(x="sex",data=tips)

                                            # Adding color to figure
# sns.set_style('white')
# sns.countplot(x="sex",data=tips)

# sns.set_style('darkgrid')
# sns.countplot(x="sex",data=tips)

                                            # Removing spines on specified side
# sns.set_style("ticks")
# sns.countplot(x="sex",data=tips)

# sns.despine(left=True,bottom=True)
# sns.countplot(x="sex",data=tips) # By Default Top and Right=True

                                            # Resizing the figure size
# plt.figure(figsize=(12,3))
# sns.countplot(x="sex",data=tips)

                                            # Scaling (Increasing the size of font)
# sns.set_context('poster')
# sns.countplot(x="sex",data=tips)

# still you're not satified with the font size
# sns.set_context("poster",font_scale=3) # font size will be 3 times bigger than poster default font
# sns.countplot(x='sex',data=tips)

# by default set_context('notebook')
plt.show()
