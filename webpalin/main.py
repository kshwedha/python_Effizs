import tkinter
from tkinter import *

main=tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
#main.geometry("300x280+300+300")

main.title('sample window(main)')


'''
    "arrow"
    "circle"
    "clock"
    "cross"
    "dotbox"
    "exchange"
    "fleur"
    "heart"
    "heart"
    "man"
    "mouse"
    "pirate"
    "plus"
    "shuttle"
    "sizing"
    "spider"
    "spraycan"
    "star"
    "target"
    "tcross"
    "trek"
    "watch"
'''

canvas= Canvas(main, width=40, height=60, cursor="tcross")
canvas.grid()
#use canvas.pack()
#use button.pack()
canvas_height=20
canvas_width=200
y=int(canvas_height/2)
canvas.create_line(0, y, canvas_width, y,fill='black', width=3)

mb =  Menubutton(main, text ="Language", relief=FLAT) 
mb.grid(row=0, column=4) 
mb.menu  =  Menu( mb, tearoff = 0 ) 
mb["menu"]  =  mb.menu 
cVar  = IntVar() 
aVar = IntVar() 
mb.menu.add_checkbutton ( label ='Kannada', variable = cVar ) 
mb.menu.add_checkbutton ( label = 'English', variable = aVar ) 
mb.grid(row=0) 


var1 = IntVar() 
Checkbutton(main, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar() 
Checkbutton(main, text='female', variable=var2).grid(row=1, sticky=W)

Label(main, text='firstname').grid(row=2, column=0)
Label(main, text='lastname').grid(row=3, column=0)
Label(main, text='Age').grid(row=4, column=0)
field1=Entry(main, width=30)
field2=Entry(main, width=30)
field3=Spinbox(main, from_=00, to=90, width=5)
field1.grid(row=2, column=1)
field2.grid(row=3, column=1)
field3.grid(row=4, column=1)

frame = Frame(main) 
frame.grid(row=0, column=1) 
bottomframe = Frame(main) 
bottomframe.grid( row=0, column=2 ) 
redbutton = Button(frame, text = 'Red', fg ='red') 
redbutton.grid( row=5, column=0) 
greenbutton = Button(frame, text = 'Brown', fg='brown') 
greenbutton.grid(row=5, column=1) 
bluebutton = Button(frame, text ='Blue', fg ='blue') 
bluebutton.grid(row=5, column=2) 
blackbutton = Button(bottomframe, text ='Black', fg ='black') 
blackbutton.grid(row=1, column=3)

Lb = Listbox(main)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.grid()

ourMessage ='This is our Message'
messageVar = Message(main, text = ourMessage) 
messageVar.config(bg='lightgreen') 
messageVar.grid(row=7, column=2 ) 


button=tkinter.Button(main, text='Stop',height=5, width=25,activebackground='black',activeforeground='green',relief=RAISED, cursor="shuttle",command=main.destroy)
#command attributes= destroy, or you can use functions without parenthesis
#font and image are 2 more attributes
button.grid(column=2)


main.mainloop()

