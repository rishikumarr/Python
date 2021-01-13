# Binary Search
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]
        if mid_number == number_to_find:
            return mid_index
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1  # if the given element Not in the list it'll return -1

# Binary Search the Time Complexity is "O(log n)" [Order(n/2)]...For Performing Binary Search given list Should be Sorted 
index=binary_search([4, 9, 11, 17, 21, 25, 29, 32, 38],21)
##################   0  1  2   3   4   5   6   7   8  ################
print(f'The Given element is present in {index}\'th index')
