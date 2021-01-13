import seaborn as sns
from matplotlib import pyplot as plt
tips=sns.load_dataset("tips")
# print(tips)

# sns.lmplot(x="total_bill",y="tip",data=tips)

                                # Adding Hue
# sns.lmplot(x="total_bill",y="tip",data=tips,hue='sex')

                                # Adding Markers
# sns.lmplot(x="total_bill",y="tip",data=tips,hue='sex',markers=['o','v'])

                                # Specifying Size To Markers
# sns.lmplot(x="total_bill",y="tip",data=tips,hue='sex',markers=['o','v'],scatter_kws={'s':100})

                                # Adding column and row
# sns.lmplot(x="total_bill",y="tip",data=tips,col='sex')  # Adding Columns

# sns.lmplot(x="total_bill",y="tip",data=tips,row="time")  # Adding Rows

# sns.lmplot(x="total_bill",y="tip",data=tips,row="time",col="sex")  # Adding Both Rows And Columns

# sns.lmplot(x="total_bill",y="tip",data=tips,row="time",col="sex")  # Adding Both Rows And Columns

                                # Adding hue
# sns.lmplot(x="total_bill",y="tip",data=tips,row="time",col="day",hue="sex")
# sns.lmplot(x="total_bill",y="tip",data=tips,col="day",hue="sex",markers=['o','v'])

                                # Adding Size To Plot
# sns.lmplot(x="total_bill",y="tip",data=tips,col="day",hue="sex",markers=['o','v'],aspect=0.6,height=8)



plt.show()
