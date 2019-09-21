#list items
l1=[(1,3),(3,2),(2,1)]
l2=[(1,7),(1,3),(3,4,5),(2,2)]

#Function to do tuple sorting
def sort_s(tup):
    return tup[-1]

#Function to do list Sorting
def listuple_sort(lis):
    #call function sort_s to do tuple sorting
    lis.sort(key=sort_s)
    return lis

#iterate each list        
for t_list in l1,l2:
    print(listuple_sort(t_list))
