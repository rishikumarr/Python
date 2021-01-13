from matplotlib import pyplot as plt

# plt.xkcd() # Cartoonic Style

plt.style.use("fivethirtyeight")

fig=plt.figure()  # empty canvas

                  # Median Developer Salaries by Age
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

                  # Developer salary
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

                 # Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.barh(age_x,py_dev_y,label="Python Developer") # horizontal bar (barh)

plt.legend() # resposible for placing labels inside canvas

plt.tight_layout()  # to avoid being conjested

plt.show() # to see the  plot in canvas
