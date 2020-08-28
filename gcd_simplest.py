#import math
#math.gcd(a,b)

def ret(a,b):
    while b:
        a,b=b,a%b
    return a

print(ret(int(input("a  :")), int(input("b  :"))))
