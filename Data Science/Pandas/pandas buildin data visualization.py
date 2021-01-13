import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

# Lets load csv files
df1=pd.read_csv("df1",index_col=0)
# print(df1)
df2=pd.read_csv("df2")
# print(df2)

#        Histogram
# df2.plot(kind='hist')
        # (or)
# df2.plot.hist()

#        Area Plot
# df2.plot.area()
# Lets add some transparency
# df2.plot.area(alpha=0.6)
        # (or)
# df2.plot(kind='area',alpha=0.6)


#        Bar Plot
# df2.plot(kind='bar',alpha=0.6)
        # (or)
# df2.plot.bar(alpha=0.6)


#        Line Plot
# df1.plot(kind='line',figsize=(12,3))
        # (or)
# df1.plot.line(figsize=(12,3))


#        Scatter Plot
# df1.plot(kind="scatter",x="A",y="B")
        # (or)
# df1.plot.scatter(x='A',y='B')

# To Differentiate A,B and C
# df1.plot.scatter(x="A",y="B",s=df1["C"]*200)


#        Box Plot
# df1.plot.box()
        # (or)
# df1.plot(kind='box')


#        KDE Bin
# df2.plot(kind="kde")
# df2['a'].plot(kind='kde')
        # (or)
# df2.plot.kde()
        # (or)
# df2.plot.density()
        # (or)
# df2.plot(kind="density")


#        HEX Bin
# df1.plot.hexbin(x="A",y="B")

# To enlarge the size of hex
# df1.plot.hexbin(x="A",y="B",gridsize=20)
        # (or)
# df1.plot(kind='hexbin',x="A",y='B',gridsize=20)

plt.show()
