import numpy as np

# print(np.array([1,2,3,4,5])) # list to 1d array

# print(np.array([[1,2,3],[4,5,6],[7,8,9]])) # list to 2D array

# print(np.arange(10)) # generate range of values

# print(np.zeros(5)) # generate zeros 1D array

# print(np.zeros((3,2))) # generate zeros 2D array

# print(np.ones(8)) # generate ones 1D array

# print(np.ones((4,5))) # generate ones 2D array

# print(np.linspace(0,10,100)) # generate equal numbers

# print(np.random.rand()) # gives a random floating point number only (positive value)

# print(np.random.rand(1,10)) # generate random floating point values

# print(np.random.rand(1,10,4)) # generate random floating point values with (10 rows 4 columns)

# print(np.random.randn()) # gives a random floating point number it maybe positive or nagative

# print(np.random.randint(10)) # gives a number 1 to 9

# print(np.random.randint(1,10,5)) # generate 5 random numbers 1 to 9 only (positive value)

# arr=np.array([[3,2,1],[4,5,6],[7,9,8]]) # this will generate a 3X3 matrix

# print(np.shape(arr)) # return a tuple (row,column)

# print(np.min(arr)) # return the lowest number in the array

# print(np.max(arr)) # return the highest number in the array

# print(np.argmax(arr)) # retuen the index of highest number in the given array

# print(np.argmin(arr)) # retuen the index of lowest number in the given array

# arr=np.array([[3,2,1],[4,5,6],[7,9,8]]) #[[3 2 1]
                                         #[4 5 6]                              [5,6]   [3,2]
                                         #[7 9 8]]   # grab 2,5,9 & [7,9,8] &  [9,8] & [4,5]

# print(arr[: ,1:2]) # output - [[2]
                             #   [5]
                             #   [9]]

# print(arr[2]) # output - [7 9 8]

# print(arr[1: ,1: ]) # output -[[5 6]
                             #   [9 8]]

# print(arr[ : 2, :2])  # output -[[3 2]
                                  #[4 5]]

# arr1=np.arange(8,15) # => [8  9 10 11 12 13 14] - grab 11

# arr2=arr1.copy() # copy
# print(arr2)

# print(arr1[3]) # output 11

# arr1[2:]=100
# print(arr1)   # => [  8   9 100 100 100 100 100] # BROADCASTING

# print(arr1%2==0) #[ True False  True False  True False  True]  # CONDITIONAL SELECTION

# print(arr1[arr1%2==0]) # output => [ 8 10 12 14] only return the values which is TRUE

# arr1=np.arange(8,15)
# arr2=np.arange(15,22)
# print(arr1+arr2) # =>[23 25 27 29 31 33 35] ARRAY WITH ARRAY

# print(arr1*100) # => [ 800  900 1000 1100 1200 1300 1400] ARRAY WITH SCALAR

# print(np.sqrt([100,9,4])) # => [10.  3.  2.]

# print(np.sum([100,9,4])) # => 113








