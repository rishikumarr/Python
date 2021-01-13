# Merge Sort
def merge_sort(elements):
    if len(elements)<=1:
        return

    mid=len(elements)//2
    left=elements[:mid]
    right=elements[mid:]
    
    merge_sort(left)
    merge_sort(right)
    merge_list(elements,left,right)

def merge_list(elements,a,b):
    i=j=k=0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            elements[k]=a[i]
            i+=1
        else:
            elements[k]=b[j]
            j+=1
        k+=1
    while i<len(a):
        elements[k]=a[i]
        i+=1
        k+=1
    while j<len(b):
        elements[k]=b[j]
        j+=1
        k+=1

elements=[100,5,8,12,56,89,7,9,45,51]
# elements=['Dog','Flemingo','Eagle','Bull','Antelope','Chameleon'] 
merge_sort(elements)
print(elements)
