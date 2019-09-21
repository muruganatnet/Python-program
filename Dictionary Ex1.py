#dictionary
bookstore = {'New Arrivals':{'COOKING':['Everyday Italian','Giada De Laurentiis','2005','30.00'],'CHILDREN':['Harry Potter','J.K.Rowling','2005','29.99'],'WEB':['Learning XML','Erik T Ray','2003','39.95']}}

#Function to do sorting
def list_sort(lis):
    return lis[-1]

#Get required items in list l1
l1=[]
for NewArr,Newinfo in bookstore.items():
    for key in Newinfo:
        l1.append((Newinfo[key]))

#Call custom sort to do sorting     
l1.sort(key=list_sort,reverse=True)

#Display as required
print('BOOKSTORE')
for i in l1:
    print(i)
    
 