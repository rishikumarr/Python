# Selection Sort
def selection_sort(elements):
    i=0
    while i<len(elements):
        min_index=i
        for j in range(i,len(elements)):
            if elements[j]<elements[min_index]:
                min_index=j
        elements[i],elements[min_index]=elements[min_index],elements[i]
        i+=1

elements=[38,9,29,7,2,15,28]
# elements=['Dog','Flemingo','Eagle','Bull','Antelope','Chameleon'] 
selection_sort(elements)
print(elements)