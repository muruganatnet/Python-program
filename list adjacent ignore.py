#list items
l1=[1,2,2,3]
l2=[2,2,3,3,3]

#Function to do sorting
def list_sort(lis):
    j=0
    templ=[]
    for i in lis:
        if j != i: 
            templ.append(i)
        j=i
    return(templ)

#Iterate each list
for lis in l1, l2:
    print(list_sort(lis))
