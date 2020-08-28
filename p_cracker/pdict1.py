#original
'''it prints the length-fit characters, if the user needs from even a single character,  put for loop
for i in range(length):
    for_loop(i,string):
'''

def for_loop(n, string):
    if n>1:
        n-=1
        for i in range(93):
            char=chr(i+33)
            string=string + char
            for_loop(n, string)
            string=string[:-1]
            #string=string.rstrip(char)

    else:
        for j in range(93):
            char=chr(j+33)
            string+=char
            c_rm=string[len(string)-1]
            f1.write("{0}\n".format(string))
            string=string[:-1]

            #print("{0}\n".format(string))
            #string=string.rstrip(char)


string=""
#try:
length=int(input("enter the length of the word:\n"))
with open("dixtion.txt","w+") as f1:
    for_loop(length, string)
f1.close()
#except:
   # print("enter the integer literal.....\n")
