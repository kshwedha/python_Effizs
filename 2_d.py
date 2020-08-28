N=int(input("enter size\n"))
a=[[int(input("col val\t")) for i in range(N)] for j in range(N)]
list_=[]
z=0

for i in range(len(a)):
    for j in range(len(a)):
        list_.append(a[i][j])
leng=len(list_)-1
for i in list_:
    if list_[leng]==i:
        leng=leng-1
    else:
        z=1
        print("false")
        break
if z==0:
    print("True")


