a=[]
while True:
    ask=input()
    if not ask:
        break
    a.append(ask)
print(a)
'''list_=list(iter(raw_input,''))
print(list_)
'''

'''a = []
prompt = "-> "

while 1:
    line=input(prompt)
    if line:
        a.append(int(line))
    else:
        break

print(a)'''

'''def read_input(prompt):
    x = input(prompt)
    while x:
        yield x
        x = input(prompt)


xs = list(map(int, read_input("-> ")))
print(xs)'''
