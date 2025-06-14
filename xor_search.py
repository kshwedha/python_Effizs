# linear Seaching by XOR
a = [8,7,2,1,1,4,5,6,9,0]
Key  = 23
for i in a:
    if not (i ^ Key):
        print("Found")
        break
else:
    print("Not Found")
