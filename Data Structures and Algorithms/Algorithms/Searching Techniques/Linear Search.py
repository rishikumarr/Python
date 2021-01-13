
def linear_search(numbers_list,number_to_find):
    for index,element in enumerate(numbers_list):
        if element==number_to_find:
            return index
    return -1 # if the given element Not in the list it'll return -1
    
# Linear Search The Time Complexity is O(n) [Order(n)]..For Performing Linear Search given list no need to be Sorted
linear=linear_search([4, 9, 11, 17, 21, 25, 29, 32, 38],25)
###############       0  1  2   3   4   5    6   7   8  ################
print(f'The Given element is present in {linear}\'th index')

