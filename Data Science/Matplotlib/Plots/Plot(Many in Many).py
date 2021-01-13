from matplotlib import pyplot as plt

# plt.xkcd() # Cartoonic Style

plt.style.use("fivethirtyeight")

fig=plt.figure()  # empty canvas

axes=fig.add_axes([0.1,0.1,0.8,0.8])  # plot the axis

axes.set_title("Salary For Developers")  # setting title for graph

axes.set_xlabel('Age')  # setting x - axis label for graph

axes.set_ylabel('Salary')  # setting y - axis label for graph

fig,axes=plt.subplots(nrows=1,ncols=3) # to create subplots (i.e creating more than one figures)

                  # Median Developer Salaries by Age
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

                 # Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]


                 # Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

axes[0].set_title("Developer Salary")
axes[0].plot(age_x,dev_y,'r')
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Salary")

axes[1].set_title("Python Developer Salary")
axes[1].plot(age_x,py_dev_y,'b')
axes[1].set_xlabel("Age")
axes[1].set_ylabel("Salary")

axes[2].set_title("JavaScript Developer Salary")
axes[2].plot(age_x,js_dev_y,'y')
axes[2].set_xlabel("Age")
axes[2].set_ylabel("Salary")

plt.legend() # resposible for placing labels inside canvas

plt.tight_layout()  # to avoid being conjested

plt.show() # to see the  plot in canvas
