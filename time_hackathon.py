'''
PROBLEM STATEMENT
Points: 30

Alice is a geeky girl. She has a lot of codes to execute but she always choose a lucky time to execute a code.

    Time is shown in 

    hour format as hh:mm:ss
    Time is said to be lucky if all the 6 characters (except ':') are different.

Given the time when she completed the code find a lucky time to execute it so that Alice need to wait as little as possible.

Input :

First line contains T, the number of test cases. Each of next T lines contains time when she completes a code (in format described above).

Output:

For each test case, output a single line containing lucky time (in format described above)

Constraints :

0<=hh<=24
0<=mm<60
0<=ss<60

3
00:00:00
12:59:59
23:59:59

SAMPLE OUTPUT

01:23:45
13:02:45
01:23:45

'''




def Time(list_):
    string=''
    x=0
    if list_[1]+list_[2]==11 and list_[4]>0:
        list_[1],list_[2]=0,1
    else:
        x=list_[1]*10+list_[2]+1
        list_[1],list_[2]=x/10,x%10
    if list_[3]+list_[4]==60:
        if list_[1] or list_[2]==0 or 1:
            list_[3],list_[4]=3,4
        else:
            list_[3],list_[4]=0,1
    else:
        x=list_[3]*10+list_[4]+1
        if list_[1] or list_[2]==x/10 or x%10:
            list_[3]=(x/10)+1
            if x%10==list_[3]:
                list_[4]=(x%10)+1
            else:
                list_[4]=x%10
        else:
            list_[3]=x/10
            if list_[3]==x%10:
                list_[4]=(x%10)+1
            else:
                list_[4]=x%10
    if (list_[5]*10)+list_[6]==60:
        if list_[1] or list_[2] or list_[3] or list_[4]==0 or 1:
            if list_[1] or loist_[2] or list_[3] or list_[4] == 3 or 4:
                list_[5],list_[6]=5,6
            else:
                list_[5],list_[6]=3,4
        else:
            list_[5], list_[6]=0,1
    else:
        x=list_[5]*10+list_[6]+1
        if list_[1] or list_[2] or list_[3] or list_[4]==x/10 or x%10:
            if list_[1] or list_[2] or list_[3] or list_[4]==(x/10)+1 or (x%10)+1:
                list_[5]=(x/10)+2
                if list_[5]!=x%10:
                    list_[6]=(x%10)+2
                else:
                    list_[6]=x%10
            else:    
                list_[5]=(x/10)+1
                if list_[5]!=x%10:
                    list_[6]=x%10
                else:
                    list_[6]=(x%10)+1
    for i in range(len(time)):
        if len(string)!=2 or 5:
            string+=time[i]
        else:
            string+=':'
    return string

def time_astro(time):
    list_=[-1]
    i=0
    while time and time.strip():
        if time[i]!=':':
            list_.append(int(time[i]))
            if len(time)-1!=i:
                i+=1
            else:
                break
        else:
            i+=1
    string1=Time(list_)
    return string1

time=str(raw_input("enter the time in hh:mm:ss format...\n"))
lucky_time=time_astro(time)
print(lucky_time)

    
