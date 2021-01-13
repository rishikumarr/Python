# Insertion Sort
def insertion_sort(elements):
    for j in range(1,len(elements)):
        current_element=elements[j]
        while elements[j]<elements[j-1] and j>0: # comparing current element with previous element 
            elements[j],elements[j-1]=elements[j-1],elements[j]
            j-=1
        elements[j]=current_element

elements=[38,9,29,7,2,15,28]
# elements=['Dog','Flemingo','Eagle','Bull','Antelope','Chameleon'] 
insertion_sort(elements)
print(elements)