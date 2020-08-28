get_user_id=""
import random
import math

def operand(rand,val):
    value=0
    if rand==0:
        value=((val*val)/(val+val))
    elif rand==1:#>=0 or rand <=5:
        value=(math.log(((val**2)*(2*val)),2))
    elif rand==2:
        value=(((2**(val/4))/((val/4)**2))/2)
    elif rand==3:
        value=((val/2)**(val/4))
    elif rand==4:
        value=(abs(((random.randint(1,99)*val)-(random.randint(1,99)*val))))
    return long(value)



def time_code(time_str):
    i=0
    value=0
    while i<len(time_str):
        val=(operand(random.randint(0,5),ord(time_str[i])))
        value=value+val
        i+=1
    return long(value)


time_str=""
with open("time_chart.txt","w+") as f:
    for i in range(93):
        time_str=chr(i+33)+"TC" #tc  or user_id(gen(charof 2))
        f.write("{0}\t{1}\n".format(time_str, str(time_code(time_str))))
        time_str=time_str.lstrip(chr(i+33))

f.close()

"""this is for strong encryption
    for i in range(93):
        time_str=chr(i+33)+"TC"
        for j in range(93):
            time_str=chr(j+33)+"TC"
            print(time str)
            time_str=time_str.lstrip(chr(j+33))
        time_str=time_str.lstrip(chr(i+33))
"""

#i.=
        
