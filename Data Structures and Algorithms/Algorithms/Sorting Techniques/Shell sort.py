# Shell Sort
def shell_sort(elements):
    gap=len(elements)//2
    while gap>0:
        for i in range(gap,len(elements)):
            current_element=elements[i]
            j=i
            while j>=gap and current_element<elements[j-gap]:
                elements[j]=elements[j-gap]
                j-=gap
            elements[j]=current_element
        gap=gap//2

elements=[100,5,8,12,56,89,7,9,45,51]
# elements=['Dog','Flemingo','Eagle','Bull','Antelope','Chameleon'] 
shell_sort(elements)
print(elements)