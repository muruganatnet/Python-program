
#List items  
l1=['axa','xyz','gg','x','yyy']
l2=['x','cd','cnc','kk']
l3=['bab','ce','cba','syanora']

#function to do sorting
def str_count(list):
    cnt=0
    for i in list:
        if len(i) >= 2 and i[0] == i[-1] :
            cnt+=1
    return cnt

#Iterate each list to do sort
for list_str in l1,l2,l3:
    print(str_count(list_str))
    
        
        
