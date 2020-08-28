def chargen(length,index,string):
    index+=1
    length=length-1
    if(length+1)>=2:
        for i in range(93):
            string+=chr(i+33)
            string=string + chargen(length,index,string)
            string-=string[len(string)-1]
    elif (length+1)== 1:
        for i in range(93):
            string+=chr(i+33)
            print(string+"\n")
            string-=string[len(string)-1]
            #string=string.substring(0,len(string)-1)


if __name__=='__main__':
    ind=-1
    string=''
    try:
        l=int(input("enter the word length\n"))
        chargen(l,ind,string)
    except:
        print("only integer literals allowed\n")


