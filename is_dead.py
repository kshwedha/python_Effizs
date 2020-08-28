def while_():
    dead=0
    bullet=6
    kill=0
    while bullet!=0 and range(walkers)<=0:
        dist.pop(min(dist))
        kill+=1
        if len(dist)==0:
            return "Rick now go asd save Carl and Judas"
        else:
            for p in range(walkers):
                walkers=walkers-1
                if range(walkers)<=0:
                    print("Good Bye Rick")
                    return kill,dead,walkers
                    break
    if bullet==0:
        time+=1
        if len(dist)==0:
        return "Rick now go asd save Carl and Judas"
        else:
            for p in range(walkers):
                walkers=walkers-1
                if range(walkers)<=0:
                    print("Good Bye Rick")
                    return kill, dead,walkers
                    break

def is_dead(dist,walkers):
    while dead==0 and range(walkers)>=1:
        kill,dead,walkers=while_()
    if range(walkers)>=1:
        print(kill)


def rick():
    dist=[]
    walkers=int(input())
    for z in range(walkers):
        dist.apppend(int(input()))
    is_dead(dist,walkers)

test_cases=int(input)
for i in range(test_cases):
    rick()

