def check_sym(list_):
    x=0
    y=0
    z=0
    size=range(len(list_))
    while x<size:
        if list_[x][y]==list_[x][size]:
            y=y+1
            size=size-1
        else:
            return "False"
            z=1
            break
    if z==0:
        while y<size:
            if list_[x][y]==list_[size][y]:
                size=size-1
                x=x+1
            else:
                return "False"
                break
    else:
        return "False"
    if z==0:
        return "True"
            
    
size=int(input())
list_=[[int(input("enter col")) for j in range(size)]for i in range(size)]
stri=check_sym(list_)
print(stri)
