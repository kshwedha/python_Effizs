
# Write your code here
a,b=input("Enter a b\n").split()
a=int(a)
b=int(b)
if a>b:
    temp=a
    a=b
    b=temp
#print(a,b)
    
if a and b:
    count=0
    i=1
    while i<=(a/2):
        i+=1
        if a%i==0:
            if b%i==0:
                #print(i)
                count+=1
            
    if b%a==0:
        print(count+2)
    else:
        print(count+1)
else:
    print("0")
                
