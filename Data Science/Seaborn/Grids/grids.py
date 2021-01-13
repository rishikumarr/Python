from matplotlib import pyplot as plt
import seaborn as sns

iris=sns.load_dataset("iris")
# print(iris)
# sns.pairplot(iris) # Pair Plot

grid=sns.PairGrid(iris)  # Pair Grid

# grid.map_diag(sns.histplot) # Distplot/histplot Diagonal(Top Left to Bottom Right)

# grid.map_upper(plt.scatter) # Top Right

# grid.map_lower(sns.kdeplot) # Bottom Left

plt.show()
