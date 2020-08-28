#a,b=map(int, input().split())
a,b=raw_input().split()
a=int(a)
b=int(b)
#a=array.split()
#print(a,b)

if a>b:
    temp=a
    a=b
    b=temp
#print(a,b)
    
if a and b:
    count=0
    i=1
    while i<=a:
        print("w")
        if a%i==0:
            print("if1")
            if b%i==0:
                print("if2")
                count+=1
                i+=1
            else:
                i+=1
        else:
            i+=1
    print(count)
else:
    print("0")
