def calculation(list_):
    total=0
    listx__=list_
    max_=max(list_)
    while total<K:
        if len(list_)!=0:
            min_=min(list_)
            total=max_-min_
            list_.remove(min_)
    if len(list_)!=0 and total<=K:
        return listx__
        
    
xlist=[]
list_=[]
calc_list=[]
def for_loop(xlist,index, list_):
    while index<length:
        index+=1
        calc_list.append(list_[index])
        listx_=calculation(list_)
        if len(listx_)>x:
            xlist=listx_
    return xlist
    calc_list.clear()
    
length=int(input("enter length\n"))
K=int(input("enter the total which must not exceed\n"))
for i in range(length):
    x=int(input("enter value\n"))
    list_.append(x)

for i in range(length):
    xlist_=for_loop(xlist,i, list_)
print("the maximum valid literal is {0}".format(xlist_))
