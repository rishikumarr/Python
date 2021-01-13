# In bubble sort the worst case is O(n square)
# Bubble Sort
def bubble_sort(elements):
    k=len(elements)
    for i in range(0,k):
        for j in range(len(elements)-1-i):
            if elements[j]>elements[j+1]:
                elements[j],elements[j+1]=elements[j+1],elements[j]
        k-=1
        
elements=[38,9,29,7,2,15,28]  # [2, 7, 9, 15, 28, 29, 38]

# We can alse pass list of words 
elements=['Dog','Flemingo','Eagle','Bull','Antelope','Chameleon'] 
# ['Antelope', 'Bull', 'Chameleon', 'Dog', 'Eagle', 'Flemingo']
# It'll return the list of elements sorted in Alphabetical Order..
# It compares each element in the list by its starting letter's ASCII value..

bubble_sort(elements)
print(elements)