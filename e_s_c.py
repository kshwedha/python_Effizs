'''
SAMPLE INPUT

4
SSSSEEEECCCCEECCCC
CCCCCSSSSEEECCCCSS
SSSSSEEESSCCCCCCCS
EESSSSCCCCCCSSEEEE

SAMPLE OUTPUT

7 9

Explanation

Longest coding streak for each day is as follows:
Day 1: 4
Day 2: 5
Day 3: 7
Day 4: 6
Maximum of these is 7, hence X is 7.

Now in order to find longest coding streak of the all days, we should also check if Roy continued his coding from previous days.
As in the sample test case, Roy was coding for 4 minutes at the end of Day 1 and he continued to code till 5 more minutes on Day 2. Hence the longest coding streak is 4+5 equals 9. There is no any other coding streak larger than this. So the longest coding streak of all days is 9.
Time Limit: 1.0 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes. '''

def keep_count(strin):
    y=0
    q=0
    i=0

    while i<len(strin):
        print("for_")
        if strin[i]=='C' or 'c':
            x=1
            y+=1
            if i+1<len(strin):
                p=i+1
                while p<len(strin) and strin[p]=='c' or 'C':
                    print("while_")
                    x+=1
                    p+=1
            i=p
            if x>q:
                q=x
        else:
            i+=1
    print(q,y)
    return q,y

test_case=4
longest_x=0
longest_y=0
for i in range(test_case):
    X,Y=keep_count("ECCECSCCCSE")#str(input()))
    if X>longest_x:
        longest_x=X
    if Y>longest_y:
        longest_y=Y
print("{0} {1}".format(longest_x,longest_y))

