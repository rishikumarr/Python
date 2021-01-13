import seaborn as sns
from matplotlib import pyplot as plt

tips=sns.load_dataset("tips")
# print(tips)  # Our tips data

flight=sns.load_dataset("flights")
# print(flight) # Our flight data

# If we want to plot this data into heat map/cluster map, we need to convert it into the matrix form
cr=tips.corr()
# print(cr)   #            total_bill       tip      size
            #total_bill    1.000000  0.675734  0.598315
            #tip           0.675734  1.000000  0.489299
            #size          0.598315  0.489299  1.000000
# Matrix form means the index and the column should be same

################################################### Heat Map #############################################################################
# Now Plot our cr matrix as heatmap

# sns.heatmap(cr)

# sns.heatmap(cr,annot=True) # plotting actual value along with heatmap

# sns.heatmap(cr,annot=True,linewidth=1,linecolor="black") # Adding some line width and line color

                                                # Adding styling to the heatmap

# sns.heatmap(cr,annot=True,linewidth=1,linecolor="black",cmap="coolwarm") # CoolWarm

# sns.heatmap(cr,annot=True,linewidths=1,linecolor="black",cmap="magma") # Magma

# fp=flight.pivot_table(index='month',columns='year',values='passengers') # Creating our own matrix table with the data(indexes,columns,values) we want

# sns.heatmap(fp) # But if you want in more specific

################################################### Cluster Map #############################################################################
# sns.clustermap(cr) # But if you want in more specific

# fp=flight.pivot_table(index='month',columns='year',values='passengers') # Creating our own matrix table with the data(indexes,columns,values) we want

# sns.clustermap(fp,standard_scale=1)


plt.show()
