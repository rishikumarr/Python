from matplotlib import pyplot as plt

# Language Popularity
# slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

# plt.pie(slices,labels=labels,)

##############################################################################################################################################################################
                                             # Adding Auto Percentage
# slices = [59219, 55466, 47544, 36443, 35917]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

# plt.pie(slices,labels=labels,autopct="%1.1f%%") #autopct="%1.1f%%" - this will add the percentage to the partitions automatically

# plt.show()

##############################################################################################################################################################################
                                            # Seperating The Part Apart a Bit
# slices = [59219, 55466, 47544, 36443, 35917]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# explode=[0,0,0,0.1,0]
# plt.pie(slices,labels=labels,explode = explode) #Seperating Python Apart a Bit

##############################################################################################################################################################################
                                            # Add Some Wedge(Border to Partitions)
# slices = [59219, 55466, 47544, 36443, 35917]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# plt.pie(slices,labels=labels,wedgeprops={'edgecolor':'black'})

##############################################################################################################################################################################
                                     # Add Some Shadow and Allign The PieChart Based On Angle
slices = [59219, 55466, 47544, 36443]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python']
colors=['#008fd5',"#fc4f30","#e5ae37","#6d904f"]
plt.pie(slices,labels=labels,colors=colors,shadow=True,startangle=90)

##############################################################################################################################################################################

plt.show()
