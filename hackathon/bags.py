print("[first line input] give no. of bags, and max candies needed for you\n")
print("[second line input] candies in each bag\n")
print("example:....\n")
print("6 9\n")
print("5 7 1 4 4 1\n")


n,x=input().split()
n,x=int(n),int(x)
sum_=x
a=[],
sub=[]
sub1=[0,0,0,0,0]
a=input().split()
for i in range(n):
        a[i]=int(a[i])
for i in range(n):
    t=int(a[i])
    #print(t)
    if t==sum_:
        sub1=t
        break
    else:
        for j in range(1,n):
            r=int(a[j])
            c=t+r
            if c==sum_:
                sub=[t,r]
                if len(sub1)>len(sub):
                    sub1.clear()
                    sub1=sub
                break
            else:
                for k in range(2,n):
                    s=int(a[k])
                    d=s+r+t
                    #print(d)
                    if d==sum_:
                        sub=[t,r,s]
                        if len(sub1)>len(sub):
                            sub1.clear()
                            sub1=sub
                        break


x=str(type(sub1))
if x[8:12]=='list':
    for i in sub1:
        print(a.index(i))
else:
    print(a.index(sub1))
    #print(a.index(str(i)))
