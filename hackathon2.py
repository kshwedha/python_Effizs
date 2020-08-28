'''
Santa was creating a new programming language . In this langauage a balance sequence of string is defined as a string in which for every opening bracket there are  

2
{}}
{}{}}}
<p><strong>2 </strong>continuous closing brackets.<br>Santa was creating a new programming language . In this langauage a balance sequence of string is defined as a string in which for every opening bracket there are
Thus <strong>{}}</strong> , <strong>{{}}}}</strong> , <strong>{{}}{}}}}</strong> are balanced , whereas <strong>}}{ , {} </strong>are not balanced . <strong>{}{}}}</strong> is not balanced as it does not have <strong>2</strong> continuous closing bracket for the first opening bracket .<br>
Now he has a sequence of brackets . He can perform only one operation on that sequence , insert an opening or closing bracket at any position .<br>
He wants to make the sequence balanced with minimum number of insert operations .<br>
Can you help him with it .<br>
<br>
<br>
<strong>Input Format:</strong></p>

'''



def solve (S):
    i=0
    count=0
    while i!=len(S):
        if S[i]=='{':
            if S[i+1]=='}':
                if S[i+2]=='}':
                    i=i+3
                elif S[i+2]=='{':
                    S=S[:i]+'}'+S[i+1:]
                    i=i+3
                    count+=1
            elif S[i+1]=='{':
                S.strip(S[i+1])
                count+=1
        elif S[i]=='}':
            if S[i+1]=='}':
                S=S[:i-1]+'{'+S[i:]
                i=i+3
                count+=1
            elif S[i+1]=='{':
                S.strip(S[i])
                count+=1
    return count

T = int(input())
for _ in range(T):
    S = input()

    out_ = solve(S)
    print (out_)
