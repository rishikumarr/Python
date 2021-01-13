from matplotlib import pyplot as plt

import numpy as np

# plt.xkcd() # Cartoonic Style

plt.style.use("fivethirtyeight")

###########################################################################################################################################
                  # Median Developer Salaries by Age
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x=np.arange(len(age_x)) # Here's our x Axis

width = 0.25

labels=["Developer salary","Python Developer salary",'JavaScript Developer salary']
                  # Developer salary
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

                 # Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

                 # Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x-width,dev_y,label=labels,width=width)

plt.bar(x,py_dev_y,label=labels,width=width)

plt.bar(x+width,js_dev_y,label=labels,width=width)

plt.title("Salary vs Age")

plt.xlabel("Age")

plt.ylabel("Salary")

plt.show()

plt.tight_layout()

plt.legend()
