#List items
l1=['bbb','ccc','axx','xzz','xaa']
l2=['mix','xyz','apple','xanadu','aardvark']

#Function to do sorting
def list_sort(lis):
    templ1=[]
    templ2=[]
    for i in lis:
        if i[0]=='x':
            templ1.append(i)
        else:
            templ2.append(i)
    templ1.sort()
    templ2.sort()
    return templ1+templ2
            
#Iterate each list
for str_list in l1,l2:
    print(list_sort(str_list))
