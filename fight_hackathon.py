def who(bob,alice):
    bob_=0
    alice_=0
    #print(bob)
    #print(alice)
    for i in range(len(bob)):
        if bob[i-1]>alice[i-1]:
            bob_+=1
        else:
            alice_+=1
    if bob_>alice_:
        return "Bob"
    elif bob_<alice_:
        return "Alice"
    else:
        return "Tie"
            

test_case=3
size=[2,4,3]
y=0
bonalice=[[1,5],[5,1],[5,6,3,1],[10,3,5,6],[15,20,50],[8,3,7]]

for z in range(len(size)):
    t=z+z
    u=z+z+1
    #print(t,u)
    bob=bonalice[t]
    #print(bob)
    alice=bonalice[u]
    #print(alice)
    who_win=who(bob,alice)
    print(who_win)
        
    
