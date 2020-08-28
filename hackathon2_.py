def solve (S):
    i=0
    count=0
    while i<len(S):
        if S[i]=='{':
            if i==len(S)-1:
                count+=1
                break
            if S[i+1]=='}':
                if i+1==len(S)-1:
                    count+=1
                    break
                if S[i+2]=='}':
                    i=i+3
                elif S[i+2]=='{':
                    i=i+2
                    count+=1
            elif S[i+1]=='{':
                if i+1==len(S)-1:
                    count+=2
                    break
                else:
                    count+=1
                    i=i+1
        elif S[i]=='}':
            if i==len(S)-1:
                count+=2
                break
            if S[i+1]=='}':
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
