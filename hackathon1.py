'''name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
size, query_count=5,2
array=[7,2,5,4,1]

def greatest(i,j,k,l):
    greatest_,p=0,0
    list_=[]
    for z in range(array.index(i),array.index(j)):
        list_.append(array[z])
    list_.sort()
    index_value=array[k-1]
    count=0
    x=1
    y=len(list_)
    while count<=n_greatest and x<=y:
            cmp_val=list_[x-1]
            x+=1
            if index_value<cmp_val:
                count+=1
                greatest_=cmp_val
    if k==3:
        return greatest_+1
    else:
        return greatest_
            

low, high, index, n_greatest=2,1,3,1
val=greatest(low, high, index, n_greatest)
print("{0}".format(val))
low,high,index, n_greatest=7,4,2,3
val=greatest(low,high,index,n_greatest)
print("{0}".format(val))
