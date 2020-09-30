
from tkinter import *

import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_int.get()):
        list1.insert(END,row)



    list1.insert("Empty Data")

window = Tk() # creating the window

l1 = Label(window,text='Title:') #filed
l1.grid(row=0,column=0)

l2 = Label(window,text='Year:')
l2.grid(row=1,column=0)

l3 = Label(window,text='Author:')
l3.grid(row=0,column=2)

l4 = Label(window,text='ISBN:')
l4.grid(row=1,column=2)

# variables
title_text = StringVar()
year_text = IntVar()
author_text = StringVar()
isbn_int = IntVar()

e1 = Entry(window, textvariable = title_text )
e1.grid(row=0,column=1)

e2 = Entry(window, textvariable = year_text)
e2.grid(row = 1, column = 1)

e3 = Entry(window, textvariable = author_text)
e3.grid(row = 0, column = 3)

e4 = Entry(window, textvariable = isbn_int)
e4.grid(row = 1, column = 3)

list1  = Listbox(window, height = 6, width =35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window, text= "View all",width =12, command=view_command)
b1.grid(row =2, column = 3)

b2 = Button(window, text= "Search entry",width =12, command = search_command)
b2.grid(row =3, column = 3)

b3 = Button(window, text= "Add entry",width =12 )
b3.grid(row =4, column = 3)

b4 = Button(window, text= "Update",width =12 )
b4.grid(row =5, column = 3)

b5 = Button(window, text= "Delete",width =12 )
b5.grid(row =6, column = 3)

b6 = Button(window, text= "Close",width =12 )
b6.grid(row =7, column = 3)





window.mainloop()