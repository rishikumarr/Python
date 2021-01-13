import numpy as np
import pandas as pd

######################################################### SERIES ############################################################################

# np.random.seed(101)  # to avoid changing data eveytime during execution
# arr=np.random.randn(3,3)
# print(arr)

# print(pd.Series(['a','b','c'],[1,2,3]))  # syntax => panda.Series(values,indexes) # indexes is optional

# print(pd.Series(['a','b','c']))

# arr=pd.Series(['a','b','c'])
# print(arr[0]) #=> a

# print(type(pd.Series(['a','b','c'])))  # => <class 'pandas.core.series.Series'>

##################################################### DATAFRAME ##############################################################################

np.random.seed(101)
arr1=pd.DataFrame(np.random.randn(4,3),['a','b','c','d'],['x','y','z'])     #             x         y         z
                                                                                #   a  2.706850  0.628133  0.907969
                                                                                #   b  0.503826  0.651118 -0.319318
                                                                                #   c -0.848077  0.605965 -2.018168
                                                                                #   d  0.740122  0.528813 -0.589001
# print(arr1['x'])  #a    2.706850           # to get column
                    #b    0.503826
                    #c   -0.848077
                    #d    0.740122
                    #Name: x, dtype: float64

# print(arr1[2:3])    #          x         y         z
                      #    c -0.848077  0.605965 -2.018168

# print(arr1.drop('d')) #          x         y         z        => this change not reflect to arr1
                        #     a  2.706850  0.628133  0.907969
                        #     b  0.503826  0.651118 -0.319318
                        #     c -0.848077  0.605965 -2.018168

# arr1.drop('y', axis =1 ,inplace=True)

# print(arr1) #           x         z     => this will affect arr1  => axis = 1 - Column
              #   a  2.706850  0.907969                             => axis = 0 - Row
              #   b  0.503826 -0.319318
              #   c -0.848077 -2.018168
              #   d  0.740122 -0.589001

# arr1.drop('c',axis=0,inplace=True)     #           x         y         z
# print(arr1)                            #     a  2.706850  0.628133  0.907969
                                         #     b  0.503826  0.651118 -0.319318
                                         #     d  0.740122  0.528813 -0.589001

# print(arr1[arr1>1])       #          x   y   z     => only return the value which return True
                            # a  2.70685 NaN NaN
                            # b      NaN NaN NaN
                            # c      NaN NaN NaN
                            # d      NaN NaN NaN

# print(arr1['a'])      # this will raise error

# print(arr1.loc['a'])      #x    2.706850          => to fetch row
                            #y    0.628133
                            #z    0.907969
                            #Name: a, dtype: float64

# print(arr1.reset_index())   #      index         x         y         z
                              #    0     a  2.706850  0.628133  0.907969
                              #    1     b  0.503826  0.651118 -0.319318
                              #    2     c -0.848077  0.605965 -2.018168
                              #    3     d  0.740122  0.528813 -0.589001

# print(arr1.set_index('z'))  #                      x         y
                              #    z
                              #     0.907969  2.706850  0.628133
                              #    -0.319318  0.503826  0.651118
                              #    -2.018168 -0.848077  0.605965
                              #    -0.589001  0.740122  0.528813

# print(arr1.loc[['d','b'],['x','z']])    #           x         z
                                          #   d  0.740122 -0.589001
                                          #   b  0.503826 -0.319318


