import random

import math
def logval(value,base):
    log_val=int(math.log(value,base))
    #math.log(value, base)
    return log_val


import time
def time_gen():
    now=time.time()
    #print("{0:10d}".format(int(now)))
    return int(now)


def rev(no):
    rem=no%10
    no=no/10
    r_num=(rem*10)+no
    return r_num

def palin():
    j=random.randint(1,8)
    i=random.randint(1,max(j,(10-j)))
    print("j:\t{0}".format(j))
    
    palindrome=((i*100)+(((i*i)+((i*2)*(j-i)))*10)+i)
    if i < j:
        num=((10+j)-i)
    else:
        num=(10+i+j)
    #print("Therefore n is {0}".format(no1))
    print(palindrome)
    return num



base=palin()
print(base)

time_now=time_gen()
print(time_now)

value=logval(time_now,base)
print(value)



