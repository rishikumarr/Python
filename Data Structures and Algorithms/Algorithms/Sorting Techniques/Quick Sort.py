def hoare_partition(elements,start,end):
    pivot_index=start
    pivot=elements[pivot_index]
    while start<end:
        while start<len(elements) and elements[start]<=pivot:
            start+=1
        while elements[end]>pivot:
            end-=1
        if start<end :
            swap(elements,start,end) 
    swap(elements,pivot_index,end)
    return end

def lomuto_partition(elements,start,end):
    pivot=elements[end]
    p_index=start
    for i in range(start,end):
        if elements[i]<=pivot:
            swap(elements,p_index,i)
            p_index+=1
    swap(elements,p_index,end)
    return p_index

def swap(elements,i,j):
    if i!=j:
        elements[i],elements[j]=elements[j],elements[i] # swapping the elements 

############################## Hoare's Partition ########################################
# def quicksort(elements,start,end):
#     if start<end:
#         p=hoare_partition(elements,start,end) # It'll return end 
#         quicksort(elements,start,p-1) # Left Side 
#         quicksort(elements,p+1,end) # Right Side  

############################## Lomuto Partition #########################################
def quicksort(elements,start,end):
    if len(elements)==1:
        return
    if start<end:
        p=lomuto_partition(elements,start,end)
        quicksort(elements,start,p-1)
        quicksort(elements,p+1,end)

elements=[11,9,29,7,2,15,28]
# elements=['Dog','Flemingo','Eagle','Bull','Antelope','Chameleon']
quicksort(elements,0,len(elements)-1)
print(elements)
